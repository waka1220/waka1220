"""表紙＋00〜11 を 1 つの .pptx（tomomeet_deck.pptx）にまとめる。

表紙は元の Google スライドの PDF 1 ページ目を画像にして入れる（元デッキのまま）。
各スライドは build_slideNN.py をそのまま実行し、保存だけ止める。
"""
import glob
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches

import slide_common

ORIGINAL_PDF = sys.argv[1] if len(sys.argv) > 1 else None

prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(5.625)

if ORIGINAL_PDF:
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-png", "-r", "200", "-f", "1", "-l", "1", "-singlefile", ORIGINAL_PDF,
                        f"{tmp}/cover"], check=True)
        cover = prs.slides.add_slide(prs.slide_layouts[6])
        cover.shapes.add_picture(f"{tmp}/cover.png", 0, 0, prs.slide_width, prs.slide_height)

slide_common.SHARED = prs
real_save = Presentation().__class__.save
Presentation().__class__.save = lambda self, *a, **k: None
try:
    for script in sorted(glob.glob("build_slide[0-9][0-9].py")):
        runpy.run_path(script)
finally:
    Presentation().__class__.save = real_save

prs.save("tomomeet_deck.pptx")
print(f"saved tomomeet_deck.pptx ({len(prs.slides)} slides)")
