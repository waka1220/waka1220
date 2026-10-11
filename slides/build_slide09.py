"""今後①（09）を、01〜08 と同じ枠で作り直す。

デバイスなしの検証を 3 ステップで見せ、比べる相手（紙のカードだけの回）を結論に置く。
"""
from slide_common import *

prs, slide = start("09", "今後①　デバイスなし", "振り返り＋ハイタッチで、マッチ率は上がるか", title_size=20)

CY, CH, CW, GAP = 1.75, 2.55, 2.1, 0.4
steps = [
    ("1　振り返り", "話した内容の\nキーワードを残し、\n誰と何を話したか\n思い出せる",
     "会話は会場のPCで処理\n外部サーバーに送らない\n（ローカルLLM）", False),
    ("2　本人が選ぶ", "相手を決めるのは\n参加者自身", "アプリが勝手に\n決めることはしない", False),
    ("3　選んだ後の一手", "選んだ相手と\nハイタッチすると、\n質問が届く",
     "ホワイトキーの\n中間印象カードを参考に、\n本人の選択を尊重する", True),
]
for i, (label, main, sub, filled) in enumerate(steps):
    x = 1.45 + i * (CW + GAP)
    card(x + CW / 2, CY, CW, CH, filled=filled, name=f"step-{i + 1}")
    text(x + 0.2, CY + 0.2, CW - 0.4, 0.22, label, size=10, color=PURPLE, bold=True)
    text(x + 0.2, CY + 0.48, CW - 0.4, 1.0, main, size=13, bold=True, line_spacing=1.1)
    text(x + 0.2, CY + 1.6, CW - 0.4, 0.8, sub, size=9, color=PURPLE, line_spacing=1.1)
    if i < len(steps) - 1:
        arrow(x + CW + 0.07, CY + CH / 2, x + CW + GAP - 0.07, CY + CH / 2, weight=2.25)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("紙のカードだけの回と、", {}), ("当日のマッチ率", {"color": PURPLE}), ("を比べる", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "まずはデバイスなしで試す。"
    "1 つ目は振り返り。話した内容のキーワードを残して、誰と何を話したか思い出せるようにする。"
    "会話は会場の PC で処理して外部サーバーには送らない（ローカル LLM）。"
    "2 つ目は、相手を決めるのは参加者自身ということ。アプリが勝手に決めることはしない。"
    "3 つ目は選んだ後の一手。選んだ相手とハイタッチすると、二人に質問が届く。"
    "ホワイトキーの中間印象カードの仕組みを参考に、本人の選択を尊重して次の一手を出す。"
    "効果は、紙のカードだけの通常の回と当日のマッチ率を比べて確かめる。"
)

prs.save("slide09_no_device.pptx")
print("saved")
