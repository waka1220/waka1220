"""今後②（10）を、01〜09 と同じ枠で作り直す。

心拍を「見る」か「感じる」か（触覚はスマートウォッチとハイタッチの 2 通り）の 4 条件を並べ、当日のマッチ率で比べる。
"""
from slide_common import *

prs, slide = start("10", "今後②　デバイスあり", "")
text(1.4, 0.88, 7.2, 0.7,
     [("相手のドキドキは、見るのと感じるのと\n", {}), ("どちらが会話のきっかけになるか", {"color": PURPLE})],
     size=18, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.1, name="title2")

text(1.45, 1.68, 7.1, 0.4,
     "前提：心拍＝感情ではない（緊張・お酒・体の動きでも変わる）。\n気持ちを読むのではなく、話のきっかけとして軽く使う",
     size=10, color=PURPLE, align=PP_ALIGN.CENTER, line_spacing=1.1)

CY, CH, GAP = 2.2, 1.75, 0.18
CW = (7.1 - GAP * 3) / 4
conds = [
    ("条件A", "なし", "", "通常の街コン\n（比較対象）", "plain"),
    ("条件B", "視覚", "画面", "相手のドキドキが\n画面に表示される", "outline"),
    ("条件C-1", "触覚", "スマートウォッチ", "相手の鼓動が\n手首に振動で届く", "filled"),
    ("条件C-2", "触覚", "ハイタッチ", "手を合わせて\n直接触れ合う", "filled"),
]
for i, (label, name, sub, desc, style) in enumerate(conds):
    x = 1.45 + i * (CW + GAP)
    if style == "filled":
        rect(x, CY, CW, CH, fill=PURPLE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1, name=f"cond-{label}")
        fg, lab = WHITE, WHITE
    else:
        rect(x, CY, CW, CH, fill=WHITE, line=GRAY if style == "plain" else PURPLE, weight=1.5,
             shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1, name=f"cond-{label}")
        fg, lab = NAVY, PURPLE
    text(x, CY + 0.15, CW, 0.22, label, size=10, color=lab, bold=True, align=PP_ALIGN.CENTER)
    text(x, CY + 0.38, CW, 0.4, name, size=20, color=fg, bold=True, align=PP_ALIGN.CENTER)
    if sub:
        text(x, CY + 0.8, CW, 0.22, sub, size=11, color=fg, bold=True, align=PP_ALIGN.CENTER)
    text(x + 0.1, CY + 1.1, CW - 0.2, 0.5, desc, size=10, color=fg, align=PP_ALIGN.CENTER, line_spacing=1.1)

C_X = 1.45 + 2 * (CW + GAP)
text(C_X, CY + CH + 0.06, 2 * CW + GAP, 0.2, "先行研究：筑波大・蜂須先生、東大・伴先生", size=8, color=PURPLE,
     align=PP_ALIGN.CENTER)
text(1.45, CY + CH + 0.06, 2 * CW + GAP, 0.2, "スマホとスマートウォッチで実現、専用ハードは不要", size=8, color=PURPLE,
     align=PP_ALIGN.CENTER)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("4条件で", {}), ("当日のマッチ率", {"color": PURPLE}), ("を比べる", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "次はデバイスありの検証。相手のドキドキを、見るのと感じるのと、どちらが会話のきっかけになるかを調べる。"
    "前提として、心拍＝感情ではない。緊張やお酒、体の動きでも変わる。"
    "なので気持ちを読むのではなく、話のきっかけとして軽く使う。"
    "条件 A は何もしない通常の街コンで、比較対象。"
    "条件 B は視覚で、相手のドキドキが画面に表示される。"
    "条件 C は触覚で、2 パターンある。C-1 はスマートウォッチで、相手の鼓動が手首に振動で届く。"
    "C-2 はハイタッチで、手を合わせて直接触れ合う。先行研究は筑波大の蜂須先生、東大の伴先生。"
    "4 条件で当日のマッチ率を比べる。スマホとスマートウォッチで実現でき、専用のハードは要らない。"
)

prs.save("slide10_with_device.pptx")
print("saved")
