"""なぜ街コンか（02）を、01 と同じ 3 者の図で作り直す。

01 では「払われない」だったお金の矢印が、当日のマッチ率という成果で
「払う理由になる」に変わる流れを見せる。
"""
from slide_common import *

prs, slide = start("02", "なぜ街コンか", "参加者にも主催者にも、満たされないニーズがある", title_size=20)
nodes("今回の案\nインタラクションで\nマッチ率を上げる")

# 矢印：TomoMeet → 顧客（成果）、顧客 → TomoMeet（お金）
arrow(A_R, ICON_Y + 0.2, A_L, ICON_Y + 0.2, name="arrow-result")
text((A_L + A_R) / 2 - 0.8, ICON_Y - 0.12, 1.6, 0.25, "当日のマッチ率", size=10, bold=True,
     align=PP_ALIGN.CENTER)
arrow(A_L, ICON_Y + 0.52, A_R, ICON_Y + 0.52, name="arrow-money")
text((A_L + A_R) / 2 - 0.8, ICON_Y + 0.6, 1.6, 0.25, [("¥ ", {}), ("払う理由になる", {"bold": True, "color": PURPLE})],
     size=10, align=PP_ALIGN.CENTER)

# 矢印：TomoMeet → 参加者（会話の支援）
arrow(B_L, ICON_Y + 0.36, B_R, ICON_Y + 0.36, name="arrow-service")
text(B_L - 0.1, ICON_Y + 0.04, B_R - B_L + 0.2, 0.25, "会話の支援", size=10, align=PP_ALIGN.CENTER)

# ---- それぞれのニーズ ----
FB_Y, FB_H, FB_W = 3.42, 0.95, 2.5
card(LX, FB_Y, FB_W, FB_H, filled=False, name="need-customer")
text(LX - FB_W / 2 + 0.15, FB_Y + 0.08, FB_W - 0.3, FB_H - 0.16,
     "参加者の満足度と\nマッチ成立を高めたい", size=13, bold=True, align=PP_ALIGN.CENTER,
     anchor=MSO_ANCHOR.MIDDLE)
card(RX, FB_Y, FB_W, FB_H, filled=True, name="need-user")
text(RX - FB_W / 2 + 0.15, FB_Y + 0.06, FB_W - 0.3, FB_H - 0.12,
     [("8", {"size": 22, "color": PURPLE}), ("分 × ", {}), ("7", {"size": 22, "color": PURPLE}), ("人\n", {}),
      ("誰に好意を感じたか\n整理できないまま次の人へ", {"size": 11, "bold": False})],
     size=12, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(CX - 1.0, FB_Y + 0.33, 2.0, 0.3, "それぞれの困りごと", size=10, color=PURPLE,
     align=PP_ALIGN.CENTER)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("両方に効く成果は", {}), ("「当日のマッチ率」", {"color": PURPLE}), ("。数字で主催者に示せる", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "街コンでは、参加者は 1 人 8 分で 7 人と話す。"
    "誰に好意を感じたかを整理できないまま次の人へ移ってしまい、メモ用紙はあっても書く余裕はない。"
    "主催者は、参加者の満足度とマッチ成立を高めたい。"
    "当日のマッチ率は両方に効く成果で、数字として主催者に示せる。"
    "だから主催者がお金を払う理由になる。"
)

prs.save("slide02_why_machikon.pptx")
print("saved")
