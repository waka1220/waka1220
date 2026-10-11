"""表紙を編集できる図形で作る（元の Google スライドの表紙と同じ構成）。"""
from pptx import Presentation
from pptx.util import Inches

import slide_common as sc
from slide_common import NAVY, PURPLE, GRAY, WHITE, PP_ALIGN, MSO_ANCHOR, MSO_SHAPE

if sc.SHARED is not None:
    prs = sc.SHARED
else:
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(5.625)
slide = prs.slides.add_slide(prs.slide_layouts[6])
sc.shapes = slide.shapes
bg = slide.background.fill
bg.solid()
bg.fore_color.rgb = GRAY

sc.rect(0.21, 0.21, 8.02, 3.64, fill=WHITE, name="frame-back")
sc.rect(1.77, 1.77, 8.02, 3.64, fill=WHITE, name="frame-front")

sc.text(1.0, 1.05, 8.0, 0.3, "関西テック 集団メンタリング", size=13, color=PURPLE, bold=True,
        align=PP_ALIGN.CENTER, name="kicker")
sc.text(0.8, 1.5, 8.4, 1.5, "対面イベントの会話を支援し、\n当日のマッチ率を上げる", size=38, bold=True,
        align=PP_ALIGN.CENTER, line_spacing=1.15, name="title")
sc.rect(2.65, 3.6, 4.7, 0.04, fill=PURPLE, name="rule")
sc.text(1.0, 3.8, 8.0, 0.35, "インタラクションでコミュニケーションを支援するアプリ", size=16,
        align=PP_ALIGN.CENTER, name="subtitle")

pill = sc.rect(6.45, 4.45, 2.85, 0.5, fill=PURPLE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5, name="presenter")
sc.text(6.45, 4.45, 2.85, 0.5, [("榎本", {"size": 15, "bold": True}), ("　NAIST ハプティクス研究", {"size": 11})],
        color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, name="presenter-text")

if sc.SHARED is None:
    prs.save("slide_cover.pptx")
    print("saved")
