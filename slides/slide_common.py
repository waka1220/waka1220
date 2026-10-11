"""スライド差し替え用の共通部品（既存デッキの配色・枠・3 者の図）。"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.oxml.ns import qn
from lxml import etree

NAVY = RGBColor(0x0A, 0x01, 0x47)    # 文字色
PURPLE = RGBColor(0x4F, 0x46, 0x9D)  # メイン
GRAY = RGBColor(0xB9, 0xC7, 0xD9)    # アクセント（背景）
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Noto Sans JP"

shapes = None  # start() で現在のスライドに差し替える


def start(number, kicker, title, title_size=24):
    """既存デッキと同じ背景・白い枠 2 枚・番号・見出しを置いたスライドを返す。"""
    global shapes
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(5.625)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    shapes = slide.shapes
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = GRAY
    rect(0.21, 0.21, 8.54, 4.165, fill=WHITE, name="frame-back")
    rect(1.25, 1.25, 8.54, 4.165, fill=WHITE, name="frame-front")
    text(0.5, 0.33, 1.4, 0.75, number, size=48, color=PURPLE, bold=True, name="number")
    text(1.4, 0.62, 7.2, 0.25, kicker, size=10, color=PURPLE, bold=True, align=PP_ALIGN.CENTER, name="kicker")
    text(1.4, 0.92, 7.2, 0.5, title, size=title_size, bold=True, align=PP_ALIGN.CENTER, name="title")
    return prs, slide


def _drop_style(shape):
    # テーマの影（effectRef）を描画側に拾わせないよう p:style ごと外す
    st = shape._element.find(qn("p:style"))
    if st is not None:
        shape._element.remove(st)


def rect(x, y, w, h, fill=None, line=None, weight=1.0, shape=MSO_SHAPE.RECTANGLE, radius=None, name=None):
    s = shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(weight)
    s.shadow.inherit = False
    _drop_style(s)
    if radius is not None:
        s.adjustments[0] = radius
    if name:
        s.name = name
    return s


def text(x, y, w, h, runs, size=14, color=NAVY, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, name=None, line_spacing=None):
    """runs: str か [(文字列, {size,color,bold}), ...] の段落リスト（\n で改段落）"""
    tb = shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    if isinstance(runs, str):
        runs = [(runs, {})]
    paras = [[]]
    for t, opt in runs:
        parts = t.split("\n")
        for i, p in enumerate(parts):
            if i > 0:
                paras.append([])
            if p:
                paras[-1].append((p, opt))
    for i, pr in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        if line_spacing:
            para.line_spacing = line_spacing
        for t, opt in pr:
            r = para.add_run()
            r.text = t
            f = r.font
            f.name = FONT
            f.size = Pt(opt.get("size", size))
            f.bold = opt.get("bold", bold)
            f.color.rgb = opt.get("color", color)
            rPr = r._r.get_or_add_rPr()
            for tag in ("a:ea",):
                el = rPr.find(qn(tag))
                if el is None:
                    el = etree.SubElement(rPr, qn(tag))
                el.set("typeface", FONT)
    if name:
        tb.name = name
    return tb


def arrow(x1, y1, x2, y2, color=PURPLE, weight=3.0, dash=False, name=None):
    c = shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = color
    c.line.width = Pt(weight)
    _drop_style(c)
    if dash:
        c.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    ln = c.line._get_or_add_ln()
    tail = etree.SubElement(ln, qn("a:tailEnd"))
    tail.set("type", "triangle")
    tail.set("w", "med")
    tail.set("len", "med")
    if name:
        c.name = name
    return c


# ---- 3 者の図：顧客（左）・TomoMeet（中央）・参加者（右） ----
LX, CX, RX = 2.75, 5.0, 7.25   # 各ノードの中心 x
ICON_Y = 1.85                   # アイコン上端
LABEL_Y = ICON_Y + 0.82
A_L, A_R = LX + 0.45, CX - 0.72  # 顧客と TomoMeet の間の矢印
B_L, B_R = CX + 0.72, RX - 0.45  # TomoMeet と参加者の間の矢印


def nodes(app_caption):
    # 顧客：ビルのアイコン
    bx, bw, bh = LX - 0.3, 0.6, 0.72
    rect(bx, ICON_Y, bw, bh, fill=WHITE, line=NAVY, weight=2.25, name="icon-building")
    for row in range(3):
        for col in range(3):
            rect(bx + 0.09 + col * 0.155, ICON_Y + 0.1 + row * 0.15, 0.1, 0.09, line=NAVY, weight=1.25)
    rect(LX - 0.07, ICON_Y + bh - 0.19, 0.14, 0.19, line=NAVY, weight=1.25)

    # 参加者：人のアイコン
    rect(RX - 0.15, ICON_Y, 0.3, 0.3, fill=WHITE, line=NAVY, weight=2.25, shape=MSO_SHAPE.OVAL, name="icon-head")
    body = rect(RX - 0.3, ICON_Y + 0.36, 0.6, 0.36, fill=WHITE, line=NAVY, weight=2.25,
                shape=MSO_SHAPE.ROUND_2_SAME_RECTANGLE, name="icon-body")
    body.adjustments[0] = 0.5

    # TomoMeet
    app = rect(CX - 0.6, ICON_Y - 0.02, 1.2, 0.76, fill=PURPLE, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
               radius=0.2, name="app")
    tf = app.text_frame
    tf.margin_left = tf.margin_right = 0
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "TomoMeet"
    r.font.name = FONT
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = WHITE

    # ノード名
    text(LX - 1.0, LABEL_Y, 2.0, 0.3, "顧客（主催者）", size=14, bold=True, align=PP_ALIGN.CENTER, name="label-customer")
    text(LX - 1.0, LABEL_Y + 0.3, 2.0, 0.25, "お金を払う人", size=11, color=PURPLE, align=PP_ALIGN.CENTER)
    text(RX - 1.0, LABEL_Y, 2.0, 0.3, "イベント参加者", size=14, bold=True, align=PP_ALIGN.CENTER, name="label-user")
    text(RX - 1.0, LABEL_Y + 0.3, 2.0, 0.25, "使う人", size=11, color=PURPLE, align=PP_ALIGN.CENTER)
    text(CX - 1.0, LABEL_Y, 2.0, 0.5, app_caption, size=10, color=PURPLE, align=PP_ALIGN.CENTER, name="label-app")


def card(cx, y, w, h, filled, name=None):
    if filled:
        return rect(cx - w / 2, y, w, h, fill=GRAY, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12, name=name)
    return rect(cx - w / 2, y, w, h, fill=WHITE, line=PURPLE, weight=1.5,
                shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12, name=name)
