"""前回のおさらい（00）。01 の前に入れる振り返り用スライド。

前回の発表スライド 2 枚（今回取り組むプロジェクト／コネクションの作り方）を並べる。
"""
from slide_common import *

prs, slide = start("00", "前回のおさらい", "前回は「探したい人を見つけて、会いに行く」アプリだった", title_size=17)

IMG_Y, IMG_W, GAP = 1.8, 3.45, 0.2
shots = [
    ("assets/prev_slide3_project.png", 1460, 826, "前回 3 枚目：今回取り組むプロジェクト"),
    ("assets/prev_slide4_steps.png", 1462, 826, "前回 4 枚目：TomoMeet を用いたコネクションの作り方"),
]
for i, (path, w, h, cap) in enumerate(shots):
    x = 1.45 + i * (IMG_W + GAP)
    ih = IMG_W * h / w
    pic = slide.shapes.add_picture(path, Inches(x), Inches(IMG_Y), Inches(IMG_W), Inches(ih))
    pic.line.color.rgb = GRAY
    pic.line.width = Pt(0.75)
    text(x, IMG_Y + ih + 0.08, IMG_W, 0.22, cap, size=9, color=PURPLE)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("今回は対象を", {}), ("街コン・婚活イベント", {"color": PURPLE}), ("に絞り直した", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "前回のおさらい。前回は、対面イベントでのネットワーキングを促進させるアプリとして TomoMeet を提案した。"
    "探したい人が誰か知る、探したい人がどこにいるのかが分かる、の 2 つが柱。"
    "使い方は、専門のタグを選ぶ、アプリが目的に合わせた人を提案する、会いたい人を選ぶ、アプリが誘導する、の 4 ステップ。"
    "今回は、対象を街コン・婚活イベントに絞り直した。なぜそうしたかを次のスライドから話す。"
)

prs.save("slide00_recap.pptx")
print("saved")
