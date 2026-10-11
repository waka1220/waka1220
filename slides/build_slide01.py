"""前回までのスライド（01）を、使う人と払う人の図入りで作り直す。

既存デッキ（Google スライド）と同じ配色・枠組みで 1 枚だけの .pptx を出力する。
Google スライドの「スライドをインポート」で差し替える想定。
"""
from slide_common import *

prs, slide = start("01", "前回まで", "使う人と、お金を払う人が違った")
nodes("前回の案\n目の前の人が誰か分かる")

# 矢印：TomoMeet → 顧客（データ）、顧客 → TomoMeet（お金、届いていない）
arrow(A_R, ICON_Y + 0.2, A_L, ICON_Y + 0.2, name="arrow-data")
text((A_L + A_R) / 2 - 0.8, ICON_Y - 0.12, 1.6, 0.25, "参加者のデータ", size=10, align=PP_ALIGN.CENTER)
arrow(A_L, ICON_Y + 0.52, A_R, ICON_Y + 0.52, color=GRAY, dash=True, name="arrow-money")
text((A_L + A_R) / 2 - 0.6, ICON_Y + 0.6, 1.2, 0.25, [("¥ ", {}), ("払われない", {"bold": True, "color": PURPLE})],
     size=10, align=PP_ALIGN.CENTER)

# 矢印：TomoMeet → 参加者（サービス）
arrow(B_L, ICON_Y + 0.36, B_R, ICON_Y + 0.36, name="arrow-service")
text(B_L, ICON_Y + 0.04, B_R - B_L, 0.25, "サービス", size=10, align=PP_ALIGN.CENTER)

# ---- フィードバック（それぞれの立場の声） ----
FB_Y, FB_H, FB_W = 3.5, 0.72, 2.5
card(LX, FB_Y, FB_W, FB_H, filled=False, name="fb-customer")
text(LX - FB_W / 2 + 0.15, FB_Y + 0.08, FB_W - 0.3, FB_H - 0.16,
     "「お金を払うほどの\nメリットが見えない」", size=13, bold=True, align=PP_ALIGN.CENTER,
     anchor=MSO_ANCHOR.MIDDLE)
card(RX, FB_Y, FB_W, FB_H, filled=True, name="fb-user")
text(RX - FB_W / 2 + 0.15, FB_Y + 0.08, FB_W - 0.3, FB_H - 0.16,
     "「誰か分かると嬉しい」", size=13, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(CX - 1.0, FB_Y + 0.22, 2.0, 0.3, "いただいたフィードバック", size=10, color=PURPLE,
     align=PP_ALIGN.CENTER)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("使う人が嬉しくても、", {}), ("払う人が嬉しくなければ", {"color": PURPLE}), ("お金は払われない", {})],
     size=17, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "前回は「目の前の人が誰か分かるアプリ」を提案した。"
    "参加者からは分かると嬉しいという声があったが、お金を払うのは主催者側。"
    "主催者にとってのメリットが見えないので、お金を払う理由にならなかった。"
    "次のスライドで、主催者側のニーズ（当日のマッチ率）を見ていく。"
)

prs.save("slide01_user_vs_customer.pptx")
print("saved")
