# -*- coding: utf-8 -*-
"""Renderer for the tailored resumes and cover letters.

Content is a list of tagged lines:

    NAME:     centred name, Comfortaa Bold
    CONTACT:  centred contact line, small
    H2:       section heading with a rule under it
    SUB:      job title, bold
    DATE:     employer and dates, italic
    P:        body paragraph, justified
    PLT:      plain left-aligned line (cover letter body, education)
    B:        bullet
    SIGN:     signature, Style Script
    SPACE:    vertical gap

**double asterisks** mark bold inside any text line.
"""

import os
import re

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                HRFlowable, KeepTogether)

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')

for name, fn in [('Nunito', 'Nunito-Regular.ttf'),
                 ('Nunito-Bold', 'Nunito-Bold.ttf'),
                 ('Nunito-Italic', 'Nunito-Italic.ttf'),
                 ('Comfortaa', 'Comfortaa-Medium.ttf'),
                 ('Comfortaa-Bold', 'Comfortaa-Bold.ttf'),
                 ('StyleScript', 'StyleScript.ttf')]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(FDIR, fn)))

addMapping('Nunito', 0, 0, 'Nunito')
addMapping('Nunito', 1, 0, 'Nunito-Bold')
addMapping('Nunito', 0, 1, 'Nunito-Italic')
addMapping('Nunito', 1, 1, 'Nunito-Bold')
addMapping('Comfortaa', 0, 0, 'Comfortaa')
addMapping('Comfortaa', 1, 0, 'Comfortaa-Bold')

BODY = 'Nunito'
HEAD = 'Comfortaa-Bold'

INK = HexColor('#1a1a1a')
SOFT = HexColor('#4a4a4a')
GREY = HexColor('#5d5d5d')
RULE = HexColor('#b9b9b9')

_BOLD = re.compile(r'\*\*(.+?)\*\*')


def _rich(text):
    """Turn **bold** into markup and escape the ampersands reportlab minds."""
    text = text.replace('&', '&amp;')
    return _BOLD.sub(r'<b>\1</b>', text)


def build_pdf(lines, path, body=9.7, lead_mult=1.40, para_gap=7.5,
              bullet_gap=3.6, entry_gap=8.5, head_gap=12, line_gap=2.4,
              margin=0.75, name_size=19, title=None):
    """Render tagged lines to a PDF.

    Every gap is its own argument rather than a multiple of one number, because
    deriving them all from a single value is what made an earlier version of
    this collapse: a tight paragraph gap dragged the bullet gap down with it.

    The type scale is deliberately short — three sizes plus the name — so the
    two faces do not read as a pile of slightly different sizes:

        name                      name_size
        headings and job titles   body + 0.6
        body text and bullets     body
        dates and contact line    body - 0.9
    """
    lead = body * lead_mult
    big = body + 0.6
    small = body - 0.9

    st = {
        'name': ParagraphStyle('name', fontName='Comfortaa-Bold',
                               fontSize=name_size, leading=name_size * 1.26,
                               alignment=TA_CENTER, textColor=INK,
                               spaceAfter=4),
        'contact': ParagraphStyle('contact', fontName=BODY, fontSize=small,
                                  leading=small * 1.3, alignment=TA_CENTER,
                                  textColor=GREY, spaceAfter=0),
        'h2': ParagraphStyle('h2', fontName=HEAD, fontSize=big,
                             leading=big * 1.25, textColor=SOFT,
                             spaceBefore=head_gap, spaceAfter=2.5),
        'sub': ParagraphStyle('sub', fontName='Nunito-Bold', fontSize=big,
                              leading=big * 1.25, textColor=INK,
                              spaceBefore=entry_gap, spaceAfter=0.5),
        'date': ParagraphStyle('date', fontName='Nunito-Italic',
                               fontSize=small, leading=small * 1.3,
                               textColor=GREY, spaceAfter=bullet_gap * 1.1),
        'p': ParagraphStyle('p', fontName=BODY, fontSize=body, leading=lead,
                            textColor=INK, spaceAfter=para_gap),
        'plt': ParagraphStyle('plt', fontName=BODY, fontSize=body,
                              leading=lead, textColor=INK,
                              spaceAfter=line_gap),
        'b': ParagraphStyle('b', fontName=BODY, fontSize=body, leading=lead,
                            textColor=INK, leftIndent=14, bulletIndent=2,
                            bulletFontName=BODY, bulletFontSize=body,
                            spaceAfter=bullet_gap),
        'sign': ParagraphStyle('sign', fontName='StyleScript', fontSize=22,
                               leading=26, textColor=INK,
                               spaceBefore=5, spaceAfter=1),
    }

    flow = []
    for line in lines:
        tag, _, text = line.partition(':')
        text = text.strip()
        if tag == 'SPACE':
            flow.append(Spacer(1, lead * 0.75))
        elif tag == 'NAME':
            flow.append(Paragraph(_rich(text), st['name']))
        elif tag == 'CONTACT':
            flow.append(Paragraph(_rich(text), st['contact']))
            flow.append(Spacer(1, 6))
        elif tag == 'H2':
            flow.append(Paragraph(_rich(text.upper()), st['h2']))
            flow.append(HRFlowable(width='100%', thickness=0.6, color=RULE,
                                   spaceBefore=0, spaceAfter=head_gap * 0.42))
        elif tag == 'SUB':
            flow.append(Paragraph(_rich(text), st['sub']))
        elif tag == 'DATE':
            flow.append(Paragraph(_rich(text), st['date']))
        elif tag == 'P':
            flow.append(Paragraph(_rich(text), st['p']))
        elif tag == 'PLT':
            flow.append(Paragraph(_rich(text), st['plt']))
        elif tag == 'B':
            flow.append(Paragraph(_rich(text), st['b'], bulletText='•'))
        elif tag == 'SIGN':
            flow.append(Paragraph(_rich(text), st['sign']))
        else:
            raise ValueError('unknown tag %r in %r' % (tag, line))

    # Keep a job title with the first line under it.
    packed, i = [], 0
    while i < len(flow):
        if (i + 1 < len(flow) and getattr(flow[i], 'style', None)
                and flow[i].style.name == 'sub'):
            packed.append(KeepTogether(flow[i:i + 3]))
            i += 3
        else:
            packed.append(flow[i])
            i += 1

    doc = SimpleDocTemplate(
        path, pagesize=letter,
        leftMargin=margin * inch, rightMargin=margin * inch,
        topMargin=margin * inch, bottomMargin=margin * inch,
        title=title or os.path.basename(path), author='Abdullah Al Zahid')
    doc.build(packed)
    return path
