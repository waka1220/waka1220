"""仮説（08）を、01〜07 と同じ枠で作り直す。

仮説（形式的な会話より、インタラクションで仲良くなれるか）を見出しに置き、検証の 2 方向をカードで並べる。
どちらも当日のマッチ率（払う人に示す数字）で確かめる、と結論でつなぐ。
"""
from slide_common import *

prs, slide = start("08", "仮説", "")
text(1.4, 0.88, 7.2, 0.7,
     [("自己紹介カードに沿った形式的な会話より、\n", {}), ("インタラクション", {"color": PURPLE}),
      ("があるほうが仲良くなれるのではないか", {})],
     size=18, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.1, name="hypothesis")

text(1.45, 1.82, 7.1, 0.5,
     "会場の道具は自己紹介カードだけで、会話は項目をなぞる形式的なものになりがち。\n"
     "二人で一緒にやるやりとりを設ければ、8分でも距離が縮まるのではないか。",
     size=12, align=PP_ALIGN.CENTER, line_spacing=1.15)

# 検証の 2 方向
CY, CH, CW, GAP = 2.55, 1.75, 3.45, 0.2
items = [
    ("検証①　デバイスなし", "振り返り＋インタラクション", "振り返って相手を選び、\n選んだ相手とハイタッチで質問が届く", "詳しくは 09", True),
    ("検証②　デバイスあり", "心拍の共有", "相手のドキドキを画面や振動で\n共有し、会話のきっかけにする", "詳しくは 10", False),
]
for i, (label, name, desc, ref, filled) in enumerate(items):
    x = 1.45 + i * (CW + GAP)
    card(x + CW / 2, CY, CW, CH, filled=filled, name=f"verify-{i + 1}")
    text(x + 0.25, CY + 0.2, CW - 0.5, 0.22, label, size=10, color=PURPLE, bold=True)
    text(x + 0.25, CY + 0.47, CW - 0.5, 0.38, name, size=15, bold=True)
    text(x + 0.25, CY + 0.92, CW - 0.5, 0.5, desc, size=11, line_spacing=1.1)
    text(x + 0.25, CY + CH - 0.32, CW - 0.5, 0.2, ref, size=9, color=PURPLE)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("どちらも", {}), ("「当日のマッチ率」", {"color": PURPLE}), ("で確かめ、主催者に示す", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "仮説は、自己紹介カードに沿った形式的な会話より、インタラクションがあるほうが仲良くなれるのではないか、ということ。"
    "04 と 07 で見たとおり、会場の道具は紙の自己紹介カードくらいで、会話は項目をなぞるものになりやすい。"
    "二人で一緒にやるやりとりを設ければ、8 分でも距離が縮まるのではないか。"
    "検証は 2 方向。1 つ目はデバイスなしで、振り返ってから選んだ相手とハイタッチすると質問が届く（09）。"
    "2 つ目はデバイスありで、心拍を共有して会話のきっかけにする（10）。"
    "どちらも当日のマッチ率で効果を確かめ、お金を払う主催者に数字で示す。"
)

prs.save("slide08_hypothesis.pptx")
print("saved")
