"""今後②（10）を、01〜09 と同じ枠で作り直す。

心拍を「見る」か「感じる」かの 3 条件を並べ、当日のマッチ率で比べる。
"""
from slide_common import *

prs, slide = start("10", "今後②　デバイスあり", "")
text(1.4, 0.88, 7.2, 0.7,
     [("相手のドキドキは、見るのと感じるのと\n", {}), ("どちらが会話のきっかけになるか", {"color": PURPLE})],
     size=18, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.1, name="title2")

text(1.45, 1.68, 7.1, 0.4,
     "前提：心拍＝感情ではない（緊張・お酒・体の動きでも変わる）。\n気持ちを読むのではなく、話のきっかけとして軽く使う",
     size=10, color=PURPLE, align=PP_ALIGN.CENTER, line_spacing=1.1)

CY, CH, CW, GAP = 2.2, 1.85, 2.2, 0.25
conds = [
    ("条件A", "なし", "通常の街コン\n（比較対象）", None, "plain"),
    ("条件B", "視覚", "相手のドキドキが画面で見え、\nそれを話題に気持ちを\n共有しやすくなる", None, "outline"),
    ("条件C", "触覚", "相手の鼓動が振動で伝わり、\nつながりを感じやすくなる", "先行研究：筑波大・蜂須先生、\n東大・伴先生", "filled"),
]
for i, (label, name, desc, ref, style) in enumerate(conds):
    x = 1.45 + i * (CW + GAP)
    if style == "filled":
        rect(x, CY, CW, CH, fill=PURPLE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1, name=f"cond-{label}")
        fg, sub = WHITE, WHITE
    else:
        rect(x, CY, CW, CH, fill=WHITE, line=GRAY if style == "plain" else PURPLE, weight=1.5,
             shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1, name=f"cond-{label}")
        fg, sub = NAVY, PURPLE
    text(x, CY + 0.15, CW, 0.22, label, size=10, color=sub, bold=True, align=PP_ALIGN.CENTER)
    text(x, CY + 0.38, CW, 0.42, name, size=22, color=fg, bold=True, align=PP_ALIGN.CENTER)
    text(x + 0.15, CY + 0.88, CW - 0.3, 0.6, desc, size=10, color=fg, align=PP_ALIGN.CENTER, line_spacing=1.1)
    if ref:
        text(x + 0.15, CY + CH - 0.42, CW - 0.3, 0.35, ref, size=8, color=fg, align=PP_ALIGN.CENTER)

text(1.45, CY + CH + 0.1, 7.1, 0.22, "スマホとスマートウォッチで実現でき、専用ハードは不要", size=10, color=PURPLE,
     align=PP_ALIGN.CENTER)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("3条件で", {}), ("当日のマッチ率", {"color": PURPLE}), ("を比べる", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "次はデバイスありの検証。相手のドキドキを、見るのと感じるのと、どちらが会話のきっかけになるかを調べる。"
    "前提として、心拍＝感情ではない。緊張やお酒、体の動きでも変わる。"
    "なので気持ちを読むのではなく、話のきっかけとして軽く使う。"
    "条件 A は何もしない通常の街コンで、比較対象。"
    "条件 B は視覚で、相手のドキドキが画面で見え、それを話題に気持ちを共有しやすくなる。"
    "条件 C は触覚で、相手の鼓動が振動で伝わり、つながりを感じやすくなる。先行研究は筑波大の蜂須先生、東大の伴先生。"
    "3 条件で当日のマッチ率を比べる。スマホとスマートウォッチで実現でき、専用のハードは要らない。"
)

prs.save("slide10_with_device.pptx")
print("saved")
