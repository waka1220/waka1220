"""現地調査（07）を、01〜06 と同じ枠で作り直す。

左にオトコン会場の写真、右に会場全体と自分のマッチ数・気づき。
参加者として欲しかったもの（会話の振り返り）を結論に置く。
"""
from slide_common import *

prs, slide = start("07", "現地調査 オトコン（男性7名・女性4名）", "全員と盛り上がったのに、自分はマッチしなかった",
                   title_size=20)

# 左：会場写真（1200×800）
IMG_X, IMG_Y, IMG_W = 1.45, 1.8, 3.1
IMG_H = IMG_W * 800 / 1200
slide.shapes.add_picture("assets/otocon_venue.jpg", Inches(IMG_X), Inches(IMG_Y), Inches(IMG_W), Inches(IMG_H))
text(IMG_X, IMG_Y + IMG_H + 0.08, IMG_W, 0.22, "オトコン会場（筆者撮影）", size=9, color=PURPLE)
text(IMG_X, IMG_Y + IMG_H + 0.32, IMG_W, 0.22, "半個室・女性固定で男性が回る・1人8分", size=11)

# 右：数字 2 つ
RX0 = 4.95
D, CY = 1.2, 1.75


def stat(x, filled, top, num, unit, bottom, name):
    fg = WHITE if filled else NAVY
    rect(x, CY, D, D, fill=PURPLE if filled else WHITE, line=None if filled else PURPLE, weight=1.75,
         shape=MSO_SHAPE.OVAL, name=name)
    text(x, CY + 0.17, D, 0.2, top, size=9, color=fg, bold=True, align=PP_ALIGN.CENTER)
    text(x, CY + 0.35, D, 0.6, [(num, {"size": 32, "color": WHITE if filled else PURPLE}), (unit, {"size": 12})],
         color=fg, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(x - 0.2, CY + D + 0.06, D + 0.4, 0.22, bottom, size=10, align=PP_ALIGN.CENTER)


stat(RX0 + 0.1, False, "会場全体", "2", "組", "マッチ成立", "stat-venue")
stat(RX0 + 1.75, True, "私", "0", "件", "全員と盛り上がった", "stat-me")

# 右：気づき
text(RX0, 3.38, 3.6, 0.22, "気づき", size=10, color=PURPLE, bold=True)
text(RX0, 3.6, 3.6, 0.55, "メモする余裕がなく、\n何を話したか忘れる", size=15, bold=True, line_spacing=1.05)
text(RX0, 4.2, 3.6, 0.22, "06 の理由3（印象の上書き）を裏づける", size=9, color=PURPLE)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("参加者として欲しかったのは", {}), ("会話の振り返り（AI議事録）", {"color": PURPLE})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "実際にオトコンに参加した。男性 7 名、女性 4 名。"
    "半個室で女性は席に固定、男性が回る形式で、1 人 8 分。"
    "会場全体では 2 組がマッチしたが（女性 4 名なので最大 4 組）、私は全員と盛り上がったのに 0 件だった。"
    "メモ用紙はあったが、書く余裕がなく、誰と何を話したか忘れてしまう。"
    "これは 06 の理由 3、話すうちに印象が上書きされることを裏づけている。"
    "参加者として一番欲しかったのは、会話の振り返り（AI 議事録）だった。"
)

prs.save("slide07_field_research.pptx")
print("saved")
