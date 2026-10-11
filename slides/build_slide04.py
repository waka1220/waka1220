"""競合（04）を、01〜03 と同じ枠で作り直す。

比較表は元のスライドの内容を引き継ぎ、右にホワイトキーの自己紹介カードを置く。
会話の最中にある道具は紙のカードだけ、という点を見せる。
"""
from slide_common import *
from pptx.oxml.ns import qn
from lxml import etree

prs, slide = start("04", "競合", "仕組みはあるが、「会話の場」には誰も介入していない", title_size=18)


def _border(cell, sides, color="B9C7D9", width_pt=1.0):
    tcPr = cell._tc.get_or_add_tcPr()
    for side in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        old = tcPr.find(qn(side))
        if old is not None:
            tcPr.remove(old)
    for side in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        ln = etree.SubElement(tcPr, qn(side))
        if side in sides:
            ln.set("w", str(int(width_pt * 12700)))
            fill = etree.SubElement(ln, qn("a:solidFill"))
            clr = etree.SubElement(fill, qn("a:srgbClr"))
            clr.set("val", sides[side] if isinstance(sides, dict) else color)
        else:
            ln.set("w", "0")
            etree.SubElement(ln, qn("a:noFill"))


def _cell(cell, runs, size=11, bold=False, color=NAVY, fill=WHITE, align=PP_ALIGN.CENTER):
    cell.fill.solid()
    cell.fill.fore_color.rgb = fill
    cell.margin_left = cell.margin_right = Inches(0.06)
    cell.margin_top = cell.margin_bottom = Inches(0.05)
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf = cell.text_frame
    tf.word_wrap = True
    if isinstance(runs, str):
        runs = [(runs, {})]
    first = True
    for t, opt in runs:
        for i, part in enumerate(t.split("\n")):
            if not first and i > 0:
                para = tf.add_paragraph()
            else:
                para = tf.paragraphs[-1]
            first = False
            para.alignment = align
            r = para.add_run()
            r.text = part
            r.font.name = FONT
            r.font.size = Pt(opt.get("size", size))
            r.font.bold = opt.get("bold", bold)
            r.font.color.rgb = opt.get("color", color)
            ea = etree.SubElement(r._r.get_or_add_rPr(), qn("a:ea"))
            ea.set("typeface", FONT)


# ---- 比較表（元スライドの内容） ----
COLS = [1.15, 1.15, 1.45, 0.95]
ROWS = [0.4, 0.62, 0.62, 0.5]
TX, TY = 1.45, 1.85
gt = slide.shapes.add_table(len(ROWS), len(COLS), Inches(TX), Inches(TY),
                            Inches(sum(COLS)), Inches(sum(ROWS)))
gt.name = "compare-table"
tbl = gt.table
tbl.first_row = False
tbl.horz_banding = False
for i, w in enumerate(COLS):
    tbl.columns[i].width = Inches(w)
for i, h in enumerate(ROWS):
    tbl.rows[i].height = Inches(h)

data = [
    ["", "出会う前", ("会話の最中", {"color": PURPLE}), "会話の後"],
    [("ホワイトキー", {"bold": True}), "AIマッチング", "紙のカード", "—"],
    [[("タメニー\n", {"bold": True}), ("オトコン提携", {"size": 10})], "アプリ登録", "—", "マッチ集計"],
    [("この提案", {"bold": True, "color": PURPLE}), "", ("インタラクション", {"bold": True, "color": WHITE}), "振り返り"],
]
for r, row in enumerate(data):
    for c, val in enumerate(row):
        runs = val if isinstance(val, list) else ([val] if isinstance(val, tuple) else val)
        cell = tbl.cell(r, c)
        highlight = (r == 3 and c == 2)
        _cell(cell, runs, bold=(r == 0), fill=PURPLE if highlight else WHITE,
              align=PP_ALIGN.LEFT if c == 0 else PP_ALIGN.CENTER)
        sides = {"a:lnB": "0A0147" if r in (2, 3) else "B9C7D9"}
        if c == 2 and r > 0:  # 「会話の最中」の列を左右の線で囲む
            sides["a:lnL"] = "4F469D"
            sides["a:lnR"] = "4F469D"
        _border(cell, sides)

text(TX, TY + sum(ROWS) + 0.12, sum(COLS), 0.25,
     "2件目の街コン：参加した瞬間にマッチングアプリへ登録", size=10, color=PURPLE)

# ---- 右：ホワイトキーの自己紹介カード（553×448） ----
IMG_X, IMG_W = 6.4, 2.1
IMG_Y = TY
slide.shapes.add_picture("assets/whitekey_profile_card.png", Inches(IMG_X), Inches(IMG_Y),
                         Inches(IMG_W), Inches(IMG_W * 448 / 553))
text(IMG_X, IMG_Y + IMG_W * 448 / 553 + 0.08, IMG_W, 0.5,
     "ホワイトキーの自己紹介カード\n会話の最中はこの紙だけ", size=10, color=PURPLE,
     align=PP_ALIGN.CENTER)

# ---- 結論 ----
text(1.45, 4.62, 7.1, 0.4,
     [("空いているのは", {}), ("「会話の最中」", {"color": PURPLE}), ("。ここに TomoMeet が入る", {})],
     size=16, bold=True, align=PP_ALIGN.CENTER, name="takeaway")

slide.notes_slide.notes_text_frame.text = (
    "ホワイトキーは出会う前に AI でマッチングし、会場では紙の自己紹介カードを交換する。"
    "タメニー（オトコン提携）は出会う前にアプリ登録、会話の後にマッチを集計する。"
    "2 件目に参加した街コンでは、参加した瞬間にマッチングアプリへの登録を求められた。"
    "どちらも会話の最中に使える道具は紙のカードくらいで、会話そのものには誰も介入していない。"
    "TomoMeet はここに、インタラクションで入る。"
)

prs.save("slide04_competitors.pptx")
print("saved")
