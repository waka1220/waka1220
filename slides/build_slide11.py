"""次にやること（11）を、00〜10 と同じ枠で作り直す。

デモ・場づくり・お願いの 3 段。最後のお願いを一番目立たせる。
"""
from slide_common import *

prs, slide = start("11", "次にやること", "10月中にデモを作り、小規模な街コンで試す", title_size=20)

X0, W = 1.45, 7.1
LABEL_W = 1.25
rows = [
    ("デモ", "振り返り＋ハイタッチ（09）と、心拍の共有（10）", "会話はローカルLLMで処理し、外部に送らない", 1.8, 0.68),
    ("場づくり", "奈良・生駒などの自治体に、イベント主催を相談する", "自治体は「お金を払う人」の候補（03）", 2.6, 0.68),
]
for label, main, sub, y, h in rows:
    rect(X0, y, W, h, fill=WHITE, line=PURPLE, weight=1.25, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.15,
         name=f"row-{label}")
    text(X0 + 0.3, y, LABEL_W, h, label, size=11, color=PURPLE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(X0 + 0.3 + LABEL_W, y + 0.1, W - LABEL_W - 0.5, 0.3, main, size=14, bold=True)
    text(X0 + 0.3 + LABEL_W, y + 0.4, W - LABEL_W - 0.5, 0.22, sub, size=10, color=PURPLE)

# お願い（一番目立たせる）
AY, AH = 3.45, 1.25
rect(X0, AY, W, AH, fill=PURPLE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12, name="ask")
text(X0 + 0.3, AY, LABEL_W, AH, "お願い", size=11, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
text(X0 + 0.3 + LABEL_W, AY + 0.17, W - LABEL_W - 0.5, 0.6,
     "街コン主催者とつながりのある方を、\n紹介していただけませんか", size=17, color=WHITE, bold=True, line_spacing=1.1)
text(X0 + 0.3 + LABEL_W, AY + 0.92, W - LABEL_W - 0.5, 0.22,
     "どの案ならお金を払うか、主催者に直接聞きたい", size=10, color=WHITE)

slide.notes_slide.notes_text_frame.text = (
    "次にやること。10 月中にデモを作り、小規模な街コンで試す。"
    "デモは、振り返り＋ハイタッチ（09）と心拍の共有（10）。会話はローカル LLM で処理して外部には送らない。"
    "場づくりとして、奈良や生駒などの自治体にイベントの主催を相談する。03 で見たとおり、自治体はお金を払う人の候補。"
    "最後にお願いです。街コンの主催者とつながりのある方がいたら、紹介していただけませんか。"
    "どの案ならお金を払うか、主催者に直接聞きたいと思っています。"
)

prs.save("slide11_next_steps.pptx")
print("saved")
