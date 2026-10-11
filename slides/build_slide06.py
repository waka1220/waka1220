"""問い（06）を、01〜05 と同じ枠で作り直す。

左に植草美幸さんの出典（アタシの婚活週報w のサムネイル）、
右に理由の候補 3 つと対応する機能を並べる。
"""
from slide_common import *

prs, slide = start("06", "問い（植草さんの説）", "なぜ「会話が盛り上がった人ほど、マッチしない」のか", title_size=18)

# 左：出典（1668×938）
IMG_X, IMG_Y, IMG_W = 1.45, 1.8, 2.9
IMG_H = IMG_W * 938 / 1668
slide.shapes.add_picture("assets/uekusa_konkatsu_shuho.jpg", Inches(IMG_X), Inches(IMG_Y), Inches(IMG_W), Inches(IMG_H))
text(IMG_X, IMG_Y + IMG_H + 0.1, IMG_W, 0.25, "婚活アドバイザー 植草美幸さん", size=11, color=PURPLE, bold=True)
text(IMG_X, IMG_Y + IMG_H + 0.38, IMG_W, 0.45,
     "出典：アタシの婚活週報w「婚活問題児が婚活パーティーへ！婚活のプロ植草美幸が愛の喝!!」",
     size=8, color=PURPLE)

# 右：理由の候補 → 対応する機能
RX0, RW = 4.65, 3.9
text(RX0 + 0.5, 1.68, 2.0, 0.22, "理由の候補", size=9, color=PURPLE, bold=True)
ROW_Y, ROW_H, GAP = 1.95, 0.74, 0.08
rows = [
    ("盛り上がりが片側だけだった", "相手の反応が見えない", "相手のドキドキを共有する", "10"),
    ("話題の面白さと、その人への関心は別", "楽しかったことを好意と取り違える", "本当にドキドキした相手に気づく", "08・10"),
    ("条件や、ほかの相手との比較で決まる", "多くの人と話すうちに印象が上書きされる", "話した内容を振り返り、次の一手へ", "09"),
]
for i, (reason, sub, feature, ref) in enumerate(rows):
    y = ROW_Y + i * (ROW_H + GAP)
    circ = rect(RX0, y + 0.06, 0.36, 0.36, fill=PURPLE, shape=MSO_SHAPE.OVAL, name=f"num-{i + 1}")
    text(RX0, y + 0.06, 0.36, 0.36, str(i + 1), size=13, color=WHITE, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(RX0 + 0.5, y, RW - 0.5, ROW_H, [
        (reason + "\n", {"size": 12, "bold": True}),
        (sub + "\n", {"size": 9}),
        ("→ " + feature, {"size": 11, "bold": True, "color": PURPLE}),
        ("  " + ref, {"size": 9, "color": PURPLE}),
    ], name=f"reason-{i + 1}")

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("盛り上がり＝好意ではない。", {}), ("そのズレを3つの機能で埋める", {"color": PURPLE})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "婚活アドバイザーの植草美幸さんは、番組「アタシの婚活週報w」で"
    "「話が弾む人はほとんどフラれます」と話している。"
    "なぜ会話が盛り上がった人ほどマッチしないのか、理由の候補は 3 つ。"
    "1 つ目は、盛り上がりが片側だけだった。相手の反応が見えないので、相手のドキドキを共有する（10）。"
    "2 つ目は、話題の面白さとその人への関心は別。楽しかったことを好意と取り違えるので、"
    "本当にドキドキした相手に気づけるようにする（08・10）。"
    "3 つ目は、条件やほかの相手との比較で決まる。多くの人と話すうちに印象が上書きされるので、"
    "話した内容を振り返って次の一手につなげる（09）。"
)

prs.save("slide06_question.pptx")
print("saved")
