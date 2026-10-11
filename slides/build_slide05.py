"""私の軸（05）を、01〜04 と同じ枠で作り直す。

応用先ごとに「使う人」と「払う人」を並べ、01 の話とつなげる。
"""
from slide_common import *

prs, slide = start("05", "私の軸", "対面で会ったとき、どれだけコミュニケーションを支援できるか", title_size=16)

# 軸の一文
pill = rect(1.45, 1.72, 7.1, 0.52, fill=WHITE, line=PURPLE, weight=1.5,
            shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5, name="axis")
text(1.45, 1.72, 7.1, 0.52, "インタラクションで、当日のマッチ率を上げるアプリ", size=16, bold=True,
     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

# 応用先 2 つ（使う人・払う人つき）
CY, CH, CW = 2.55, 1.8, 3.2


def stage(x, filled, label, place, user, payer, name):
    card(x + CW / 2, CY, CW, CH, filled=filled, name=name)
    text(x, CY + 0.18, CW, 0.25, label, size=10, color=PURPLE, bold=True, align=PP_ALIGN.CENTER)
    text(x, CY + 0.42, CW, 0.4, place, size=15, bold=True, align=PP_ALIGN.CENTER)
    for i, (k, v) in enumerate([("使う人", user), ("払う人", payer)]):
        y = CY + 1.0 + i * 0.36
        text(x + 0.3, y, 0.7, 0.3, k, size=10, color=PURPLE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        text(x + 0.95, y, CW - 1.1, 0.3, v, size=12, bold=(k == "払う人"), anchor=MSO_ANCHOR.MIDDLE)


stage(1.45, True, "最初の応用先", "街コン・婚活イベント", "参加者", "主催者・自治体", "stage-first")
arrow(4.75, CY + CH / 2, 5.25, CY + CH / 2, name="arrow-next")
stage(5.35, False, "ゆくゆくは", "マッチングアプリで会った後", "アプリの利用者", "アプリの運営会社",
      "stage-later")

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("どの場面でも、", {}), ("払う人にはマッチ率という数字", {"color": PURPLE}), ("で価値を示す", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "私の軸は、対面で会ったときにどれだけコミュニケーションを支援できるか。"
    "アプリとしては、インタラクションで当日のマッチ率を上げる。"
    "最初は街コン・婚活イベントで試す。使うのは参加者、お金を払うのは主催者や自治体。"
    "ゆくゆくは、マッチングアプリで出会った二人が実際に会う場面にも広げたい。"
    "その場合、お金を払うのはマッチングアプリの運営会社になる。"
    "どちらの場面でも、払う人にはマッチ率という数字で価値を示す。"
)

prs.save("slide05_my_axis.pptx")
print("saved")
