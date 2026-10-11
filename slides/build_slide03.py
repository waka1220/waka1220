"""社会的背景（03）を、01・02 と同じ枠で作り直す。

TOKYO縁結びのメインビジュアルを左に置き、右に概要と数字をまとめる。
結論で「自治体も払う人になりうる」とつなぎ、11 の自治体への相談に橋渡しする。
"""
from slide_common import *

prs, slide = start("03", "社会的背景・政策的追い風", "行政も出会いの支援に乗り出している")

# 左：TOKYO縁結びのビジュアル（1240×1000）
IMG_W = 3.0
slide.shapes.add_picture("assets/tokyo_enmusubi.png", Inches(1.5), Inches(1.75), Inches(IMG_W), Inches(IMG_W * 1000 / 1240))

# 右：概要と数字
RX0, RW = 4.9, 3.65
text(RX0, 1.8, RW, 0.3, "東京都「TOKYO縁結び」", size=13, color=PURPLE, bold=True)
text(RX0, 2.12, RW, 0.85, "2024年9月開始。\n価値観診断をもとにAIが相手を紹介する、\n都運営の婚活アプリ",
     size=13, bold=True, line_spacing=1.1)
text(RX0, 3.02, RW, 0.25, "登録料 11,000円／2年間", size=11)

text(RX0, 3.35, 1.25, 0.6, [("約", {"size": 14}), ("7", {"size": 36}), ("割", {"size": 14})],
     size=14, color=PURPLE, bold=True, anchor=MSO_ANCHOR.BOTTOM, name="stat")
text(RX0 + 1.3, 3.5, RW - 1.3, 0.45, "結婚に関心があっても\n行動に移せていない", size=12, bold=True,
     anchor=MSO_ANCHOR.BOTTOM)
text(RX0, 4.05, RW, 0.2, "「約7割」は東京都の調査（TOKYO縁結び開始時の発表より）", size=8, color=PURPLE)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("自治体も", {}), ("「お金を払う人」", {"color": PURPLE}), ("の候補になる", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "東京都は 2024 年 9 月から、都が運営する婚活アプリ「TOKYO縁結び」を始めた。"
    "価値観診断をもとに AI が相手を紹介する仕組みで、登録料は 2 年間で 11,000 円。"
    "都の調査では、結婚に関心があっても行動に移せていない人が約 7 割いる。"
    "行政が出会いの支援に予算を出しているということは、自治体も TomoMeet にお金を払う人の候補になる。"
)

prs.save("slide03_tokyo_enmusubi.pptx")
print("saved")
