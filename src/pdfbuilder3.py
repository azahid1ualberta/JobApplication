# -*- coding: utf-8 -*-
"""Renderer for the tailored resumes and cover letters.

Content is a list of tagged lines:

    NAME:     centred name, Comfortaa Bold
    CONTACT:  centred contact line, small
    H2:       section heading with a rule under it
    SUB:      job title, bold
    DATE:     employer and dates, italic
    P:        body paragraph
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

# Vertical rhythm, fitted to the original August 117073 render: every line
# lands within 2px of the original at 105dpi, and the page ends at the same
# 731.7pt. Line breaks match the originals exactly on both documents.
FIRST_GAP = 11.4     # contact line to the first heading, in total
H2_AFTER = 5.0       # heading to its rule
SUB_AFTER = 1.0      # job title to its date line
RULE_AFTER = 4.2     # rule to the first line under it
SUB_BEFORE = 0.65    # space above a job title, as a fraction of head_before
DATE_EXTRA = 1.5     # date line to first bullet, on top of space_after
BULLET_EXTRA = 0.0   # between bullets, on top of space_after
PLT_AFTER = 0.6      # between plain lines: the letter's address block
SPACE_MULT = 0.55    # a SPACE line, as a fraction of the body leading
SIGN_BEFORE = 1.0    # 'Sincerely,' to the signature
SIGN_AFTER = 4.0     # signature to the typed name

_BOLD = re.compile(r'\*\*(.+?)\*\*')


def _rich(text):
    """Turn **bold** into markup and escape the ampersands reportlab minds."""
    text = text.replace('&', '&amp;')
    return _BOLD.sub(r'<b>\1</b>', text)


def build_pdf(lines, path, body_size=10, leading_mult=1.36, space_after=8,
              margin=0.9, head_before=11, top_margin=0.6, name_size=16,
              title=None):
    """Render tagged lines to a PDF.

    These are the parameters the original generators used, and the style ratios
    below are calibrated against the original August renders so the output
    matches them: a 16pt name, headings slightly smaller than the job titles,
    and a full `space_after` between bullets.

    Type scale for a 9.3pt resume body:

        name                 16    Comfortaa Bold
        job titles           10.0  Nunito Bold          body + 0.7
        body and bullets     9.3   Nunito               body
        section headings     9.0   Comfortaa Bold caps  body - 0.3
        dates                8.75  Nunito Italic        body - 0.55
        contact line         8.6   Nunito
    """
    lead = body_size * leading_mult
    head = body_size - 0.3
    sub = body_size + 0.7
    date = body_size - 0.55
    top = top_margin

    st = {
        'name': ParagraphStyle('name', fontName='Comfortaa-Bold',
                               fontSize=name_size, leading=name_size * 1.25,
                               alignment=TA_CENTER, textColor=INK,
                               spaceAfter=4),
        'contact': ParagraphStyle('contact', fontName=BODY, fontSize=8.6,
                                  leading=11, alignment=TA_CENTER,
                                  textColor=GREY, spaceAfter=5),
        'h2': ParagraphStyle('h2', fontName=HEAD, fontSize=head,
                             leading=head * 1.2, textColor=SOFT,
                             spaceBefore=head_before, spaceAfter=H2_AFTER),
        'sub': ParagraphStyle('sub', fontName='Nunito-Bold', fontSize=sub,
                              leading=sub * 1.25, textColor=INK,
                              spaceBefore=head_before * SUB_BEFORE, spaceAfter=SUB_AFTER),
        'date': ParagraphStyle('date', fontName='Nunito-Italic',
                               fontSize=date, leading=date * 1.25,
                               textColor=GREY, spaceAfter=space_after + DATE_EXTRA),
        'p': ParagraphStyle('p', fontName=BODY, fontSize=body_size,
                            leading=lead, textColor=INK,
                            spaceAfter=space_after),
        'plt': ParagraphStyle('plt', fontName=BODY, fontSize=body_size,
                              leading=lead, textColor=INK, spaceAfter=PLT_AFTER),
        'b': ParagraphStyle('b', fontName=BODY, fontSize=body_size,
                            leading=lead, textColor=INK, leftIndent=12,
                            bulletIndent=2.5, bulletFontName=BODY,
                            bulletFontSize=body_size,
                            spaceAfter=space_after + BULLET_EXTRA),
        'sign': ParagraphStyle('sign', fontName='StyleScript', fontSize=21,
                               leading=25, textColor=INK,
                               spaceBefore=SIGN_BEFORE, spaceAfter=SIGN_AFTER),
    }

    st['h2_first'] = ParagraphStyle('h2_first', parent=st['h2'], spaceBefore=0)

    flow = []
    prev_tag = None
    for line in lines:
        tag, _, text = line.partition(':')
        text = text.strip()
        if tag == 'SPACE':
            flow.append(Spacer(1, lead * SPACE_MULT))
        elif tag == 'NAME':
            flow.append(Paragraph(_rich(text), st['name']))
        elif tag == 'CONTACT':
            flow.append(Paragraph(_rich(text), st['contact']))
        elif tag == 'H2':
            if prev_tag == 'CONTACT':
                # a spacer stops reportlab collapsing the two gaps, so set
                # the whole distance here and drop the heading's own space
                flow.append(Spacer(1, FIRST_GAP - st['contact'].spaceAfter))
                flow.append(Paragraph(_rich(text.upper()), st['h2_first']))
            else:
                flow.append(Paragraph(_rich(text.upper()), st['h2']))
            flow.append(HRFlowable(width='100%', thickness=0.6, color=RULE,
                                   spaceBefore=0, spaceAfter=RULE_AFTER))
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
        prev_tag = tag

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
        topMargin=top * inch, bottomMargin=margin * inch,
        title=title or os.path.basename(path), author='Abdullah Al Zahid')
    doc.build(packed)
    return path
