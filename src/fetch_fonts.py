# -*- coding: utf-8 -*-
"""Fetch the four typefaces and cut the static instances the renderer needs.

The variable fonts come from the Google Fonts repository; reportlab cannot read
a variable font directly, so each weight is instanced out to its own file.
Writes into src/fonts/. Run once after cloning:

    pip install fonttools
    python src/fetch_fonts.py
"""

import os
import shutil
import urllib.request

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

BASE = "https://raw.githubusercontent.com/google/fonts/main/"
FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

SOURCES = {
    "Comfortaa.ttf": "ofl/comfortaa/Comfortaa%5Bwght%5D.ttf",
    "Nunito.ttf": "ofl/nunito/Nunito%5Bwght%5D.ttf",
    "Nunito-Italic.ttf": "ofl/nunito/Nunito-Italic%5Bwght%5D.ttf",
    "StyleScript.ttf": "ofl/stylescript/StyleScript-Regular.ttf",
}

INSTANCES = [
    ("Nunito.ttf", 400, "Nunito-Regular.ttf"),
    ("Nunito.ttf", 700, "Nunito-Bold.ttf"),
    ("Nunito-Italic.ttf", 400, "Nunito-Italic.ttf"),
    ("Comfortaa.ttf", 500, "Comfortaa-Medium.ttf"),
    ("Comfortaa.ttf", 700, "Comfortaa-Bold.ttf"),
]


def main():
    os.makedirs(FDIR, exist_ok=True)
    for name, path in SOURCES.items():
        dest = os.path.join(FDIR, name)
        urllib.request.urlretrieve(BASE + path, dest)
        print("downloaded", name)

    for src, wght, out in INSTANCES:
        if src == out:
            tmp = os.path.join(FDIR, "_" + out)
            shutil.copy(os.path.join(FDIR, src), tmp)
            src_path = tmp
        else:
            src_path = os.path.join(FDIR, src)
        font = TTFont(src_path)
        # updateFontNames matters: without it every instance keeps the
        # variable font's name and reportlab resolves bold to the wrong file.
        instantiateVariableFont(font, {"wght": wght}, inplace=True,
                                updateFontNames=True)
        font.save(os.path.join(FDIR, out))
        print("instanced", out, "->", font["name"].getDebugName(4))
        if src_path.startswith(os.path.join(FDIR, "_")):
            os.remove(src_path)


if __name__ == "__main__":
    main()
