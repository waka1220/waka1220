"""表紙＋00〜11 を 1 つの .pptx（tomomeet_deck.pptx）にまとめる。

表紙も build_cover.py で編集できる図形として作る。
各スライドは build_slideNN.py をそのまま実行し、保存だけ止める。
"""
import glob
import runpy

from pptx import Presentation
from pptx.util import Inches

import slide_common


prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(5.625)

slide_common.SHARED = prs
runpy.run_path("build_cover.py")
real_save = Presentation().__class__.save
Presentation().__class__.save = lambda self, *a, **k: None
try:
    for script in sorted(glob.glob("build_slide[0-9][0-9].py")):
        runpy.run_path(script)
finally:
    Presentation().__class__.save = real_save

prs.save("tomomeet_deck.pptx")
print(f"saved tomomeet_deck.pptx ({len(prs.slides)} slides)")
