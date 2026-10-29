# -*- coding: utf-8 -*-
"""Shared builders for Living Earth unit Printables, Student Notebook, Teacher Key (PDF)
and Teacher Plan / Key (HTML for Google Docs conversion)."""
from reportlab import rl_config
rl_config.useA85 = 0
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, KeepInFrame, Flowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import html as _html

FD = '/usr/share/fonts/truetype/dejavu/'

GREY = colors.Color(0.38, 0.38, 0.38)
BLACK = colors.black
W, H = letter
MARGIN = 0.6 * inch
CW = W - 2 * MARGIN

S = {
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.2, leading=12.2, alignment=TA_LEFT),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=7.6, leading=9.8, textColor=GREY),
    'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=8.8, leading=11.2),
    'cellb': ParagraphStyle('cellb', fontName='Helvetica-Bold', fontSize=8.8, leading=11.2),
    'kick': ParagraphStyle('kick', fontName='Helvetica-Bold', fontSize=7.6, leading=10, textColor=GREY),
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=14.5, leading=18),
    'h': ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=9.6, leading=12.5, spaceBefore=4),
    'h1': ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=17, leading=21, spaceAfter=6),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11.5, leading=15, spaceBefore=8, spaceAfter=3),
    'use': ParagraphStyle('use', fontName='Helvetica-Oblique', fontSize=8.4, leading=11, textColor=GREY),
    'q': ParagraphStyle('q', fontName='Helvetica-Bold', fontSize=10.2, leading=13.4),
    'lab': ParagraphStyle('lab', fontName='Helvetica-Bold', fontSize=8.6, leading=11),
    'hint': ParagraphStyle('hint', fontName='Helvetica-Oblique', fontSize=7.8, leading=10, textColor=GREY),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=8.8, leading=11.6, leftIndent=8),
}


def san(t):
    return str(t).replace('\u2192', '->').replace('\u2702 ', '').replace('\u2702', '')


def esc(t):
    return _html.escape(t, quote=False)


def P(text, style='body'):
    return Paragraph(san(text).replace('\n', '<br/>'), S[style])


def cellp(t, bold=False):
    return Paragraph(san(t).replace('\n', '<br/>'), S['cellb' if bold else 'cell'])


# ---------- generic block rendering ----------
def dash_style(extra=None):
    st = [('BOX', (0, 0), (-1, -1), 0.9, BLACK, None, (3, 3))]
    return TableStyle(st + (extra or []))


def blk_table(b, width):
    header, rows = b['header'], b['rows']
    cw = b.get('cols')
    ncol = len(header or rows[0])
    if cw:
        tot = float(sum(cw))
        cws = [width * c / tot for c in cw]
    else:
        cws = [width / ncol] * ncol
    data = []
    if header:
        data.append([cellp(h, True) for h in header])
    for r in rows:
        data.append([cellp(c) for c in r])
    rh = b.get('rowh')
    t = Table(data, colWidths=cws, rowHeights=None if not rh else
              ([None] if header else []) + [rh * inch] * len(rows))
    st = [('GRID', (0, 0), (-1, -1), 0.6, BLACK), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    if header:
        st.append(('LINEBELOW', (0, 0), (-1, 0), 1.3, BLACK))
    t.setStyle(TableStyle(st))
    return t


def blk_lines(n, width, gap=0.27):
    t = Table([[''] for _ in range(n)], colWidths=[width], rowHeights=[gap * inch] * n)
    t.setStyle(TableStyle([('LINEBELOW', (0, 0), (-1, -1), 0.5, BLACK)]))
    return t


def blk_box(h, width, label=None, dashed=True):
    t = Table([[P(label, 'hint') if label else '']], colWidths=[width], rowHeights=[h * inch])
    t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.9, BLACK, None, (3, 3) if dashed else None),
                           ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
    return t


def blk_cards(texts, cols, width, h=0.62):
    rows = []
    row = []
    for tx in texts:
        row.append(Paragraph(san(tx), S['cellb']))
        if len(row) == cols:
            rows.append(row)
            row = []
    if row:
        row += [''] * (cols - len(row))
        rows.append(row)
    t = Table(rows, colWidths=[width / cols] * cols, rowHeights=[h * inch] * len(rows))
    t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.9, BLACK, None, (3, 3)),
                           ('INNERGRID', (0, 0), (-1, -1), 0.9, BLACK, None, (3, 3)),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
    return t


def blk_punnett(b, width):
    """2x2 Punnett grid. b: top=[a,b], side=[a,b], cells=[[..],[..]] or None (blank), title."""
    top, side = b['top'], b['side']
    cells = b.get('cells') or [['', ''], ['', '']]
    cs = 0.78 * inch
    data = [['', cellp(top[0], True), cellp(top[1], True)],
            [cellp(side[0], True), cellp(cells[0][0]), cellp(cells[0][1])],
            [cellp(side[1], True), cellp(cells[1][0]), cellp(cells[1][1])]]
    t = Table(data, colWidths=[0.45 * inch, cs, cs], rowHeights=[0.3 * inch, 0.62 * inch, 0.62 * inch])
    t.setStyle(TableStyle([('GRID', (1, 1), (-1, -1), 0.9, BLACK), ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LINEBELOW', (1, 0), (-1, 0), 0.5, BLACK),
                           ('LINEAFTER', (0, 1), (0, -1), 0.5, BLACK)]))
    if b.get('title'):
        wrap = Table([[P(b['title'], 'lab')], [t]], colWidths=[2.2 * inch])
        wrap.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0)]))
        return wrap
    return t


def render_blocks(blocks, width):
    out = []
    pend = []  # punnett side-by-side buffer

    def flush():
        if pend:
            t = Table([pend[:]], colWidths=[2.4 * inch] * len(pend), hAlign='LEFT')
            t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0)]))
            out.append(t)
            out.append(Spacer(1, 5))
            pend.clear()

    for b in blocks:
        k = b[0] if isinstance(b, tuple) else b['k']
        if k != 'punnett':
            flush()
        if k == 'p':
            out.append(P(b[1]))
            out.append(Spacer(1, 3))
        elif k == 'h':
            out.append(P(b[1], 'h'))
        elif k == 'note':
            out.append(P(b[1], 'small'))
            out.append(Spacer(1, 2))
        elif k == 'lines':
            out.append(blk_lines(b[1], width))
            out.append(Spacer(1, 4))
        elif k == 'table':
            out.append(blk_table(b[1], width))
            out.append(Spacer(1, 6))
        elif k == 'cards':
            out.append(blk_cards(b[1], b[2], width, b[3] if len(b) > 3 else 0.62))
            out.append(Spacer(1, 6))
        elif k == 'box':
            out.append(blk_box(b[1], width, b[2] if len(b) > 2 else None))
            out.append(Spacer(1, 5))
        elif k == 'punnett':
            pend.append(blk_punnett(b[1], width))
        elif k == 'gap':
            out.append(Spacer(1, b[1] * inch))
        else:
            raise ValueError(k)
    flush()
    return out


# ---------- document scaffolding ----------
def make_doc(path, title, footer):
    doc = BaseDocTemplate(path, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=0.7 * inch, title=title, pageCompression=1,
                          author='Living Earth')

    def on_page(c, d):
        c.saveState()
        c.setFont('Helvetica', 7)
        c.setFillColor(GREY)
        c.drawString(MARGIN, 0.4 * inch, footer)
        c.drawRightString(W - MARGIN, 0.4 * inch, 'Page %d' % d.page)
        c.restoreState()

    doc.addPageTemplates([PageTemplate(id='p', frames=[Frame(MARGIN, 0.7 * inch, CW, H - MARGIN - 0.7 * inch, id='f',
                                                              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)],
                                        onPage=on_page)])
    return doc


def item_frame(content, width, maxh):
    inner = KeepInFrame(width - 16, maxh - 16, content, mode='shrink')
    t = Table([[inner]], colWidths=[width])
    t.setStyle(dash_style([('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                           ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    return t


def item_head(unit, it):
    return [P('UNIT %s · LESSON %d · %s' % (unit['id'], it['lesson'], it['kicker'].upper()), 'kick'),
            P(esc(it['title']), 'title'),
            P('Use: %s · Copies: %s' % (esc(it['use']), esc(it['copies'])), 'use'),
            Spacer(1, 6)]


def build_printables(unit, path):
    doc = make_doc(path, 'Unit %s Printables' % unit['id'], 'Unit %s · %s · Printables' % (unit['id'], unit['name']))
    st = []
    st.append(P('Unit %s Printables: %s' % (unit['id'], esc(unit['name'])), 'h1'))
    st.append(P(esc(unit['std_line']), 'body'))
    st.append(Spacer(1, 4))
    st.append(P('Everything the class needs for this unit is in this one file, organized by lesson. '
                'Print on white paper in black ink only. "Copies" says how many to print: per student, per pair, per group or one for the class. '
                'Each item is a dashed box; cut cards along the dashed lines. Sources are cited on any item that uses real data; '
                'items marked illustrative use simplified numbers made up for class.', 'body'))
    st.append(Spacer(1, 8))
    rows = [[str(it['lesson']), it['title'], it['use'], it['copies']] for it in unit['items']]
    st.append(blk_table({'header': ['Lesson', 'Printable', 'Use', 'Copies'], 'rows': rows, 'cols': [0.95, 3.2, 3.0, 1.4]}, CW))
    st.append(Spacer(1, 8))
    st.append(P('Lessons with no printable (%s) use the notebook and the slides only.' % ', '.join(
        '%d' % l['n'] for l in unit['lessons'] if not any(i['lesson'] == l['n'] for i in unit['items'])), 'small'))
    st.append(PageBreak())
    for i, it in enumerate(unit['items']):
        body = item_head(unit, it) + render_blocks(it['body'], CW - 16)
        st.append(item_frame(body, CW, H - MARGIN - 0.7 * inch - 4))
        if i < len(unit['items']) - 1:
            st.append(PageBreak())
    doc.build(st)


# ---------- notebook ----------
def nb_header(unit, lesson_label, side, title):
    t = Table([[P('UNIT %s · %s · %s PAGE' % (unit['id'], lesson_label.upper(), side), 'kick'),
                P('Page ______', 'kick')]], colWidths=[CW * 0.78, CW * 0.22])
    t.setStyle(TableStyle([('ALIGN', (1, 0), (1, 0), 'RIGHT'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 0)]))
    nm = P('Name ______________________   Period ______   Date ____________', 'small')
    return [t, nm, Spacer(1, 4), P(esc(title), 'title'), Spacer(1, 3)]


def nb_section(label, hint, h, kind='box'):
    """labelled box. kind: box (solid), glue (dashed), lines."""
    h = h * 1.38
    items = [P(esc(label), 'lab')]
    if hint:
        items.append(P(esc(hint), 'hint'))
    if kind == 'lines':
        n = max(1, int(h / 0.27))
        items.append(blk_lines(n, CW))
    else:
        items.append(blk_box(h, CW, None, dashed=(kind == 'glue')))
    items.append(Spacer(1, 5))
    return items


def nb_page(unit, lesson_label, side, title, focus, secs, avail=H - MARGIN - 0.7 * inch):
    st = nb_header(unit, lesson_label, side, title)
    st.append(P('Focus question: ' + esc(focus), 'q'))
    st.append(Spacer(1, 5))
    for s in secs:
        st += nb_section(*s)
    return [KeepInFrame(CW, avail, st, mode='shrink')]


def build_notebook(unit, path):
    doc = make_doc(path, 'Unit %s Student Notebook' % unit['id'],
                   'Unit %s · %s · Student Notebook' % (unit['id'], unit['name']))
    st = []
    first = True
    for l in unit['lessons']:
        nb = l['nb']
        lab = 'Lesson %d' % l['n']
        spreads = [(lab, l['title'], l['focus'], nb['left'], nb['right'], l.get('warmup'), l.get('exit'), '')]
        if nb.get('part2'):
            p2 = nb['part2']
            spreads.append((lab + ' Part 2', l['title'] + ': Reading Notes', p2['focus'], p2['left'], p2['right'],
                            p2.get('warmup'), p2.get('exit'), ' (continued)'))
        for (lb, ti, fq, left, right, wu, ex, _) in spreads:
            lsecs = []
            if wu:
                lsecs.append((wu[0], wu[1], 1.0, 'lines'))
            lsecs += left
            rsecs = list(right)
            single = not right
            if ex:
                (lsecs if single else rsecs).append((ex[0], ex[1], 1.0, 'lines'))
            if not first:
                st.append(PageBreak())
            first = False
            if single:
                st += nb_page(unit, lb, 'REFLECTION', ti, fq, lsecs)
            else:
                st += nb_page(unit, lb, 'LEFT', ti, fq, lsecs)
                st.append(PageBreak())
                st += nb_page(unit, lb, 'RIGHT', ti + ' (continued)', fq, rsecs)
    doc.build(st)


# ---------- key ----------
def build_key(unit, path):
    doc = make_doc(path, 'Unit %s Printables Teacher Key' % unit['id'],
                   'Unit %s · %s · Printables Teacher Key' % (unit['id'], unit['name']))
    st = [P('Unit %s Printables Teacher Key: %s' % (unit['id'], esc(unit['name'])), 'h1')]
    st.append(P(esc(unit['std_line']), 'body'))
    st.append(Spacer(1, 4))
    st.append(P('Data caveats', 'h2'))
    for c in unit['caveats']:
        st.append(P('• ' + c, 'body'))
        st.append(Spacer(1, 2))
    st.append(P('How to use this key', 'h2'))
    st.append(P('Items are in lesson order and match the Printables index. Sample answers are model answers, not the only acceptable wording: '
                'accept any answer that uses the evidence correctly. Notebook warm-ups and exit tickets are listed under each lesson.', 'body'))
    for l in unit['lessons']:
        st.append(PageBreak())
        st.append(P('Lesson %d: %s' % (l['n'], esc(l['title'])), 'h1'))
        st.append(P('Targets: ' + esc('; '.join(l['target_labels'])), 'use'))
        st.append(Spacer(1, 4))
        its = [i for i in unit['items'] if i['lesson'] == l['n']]
        for it in its:
            st.append(P(esc(it['title']), 'h2'))
            st += render_blocks(it['key'], CW)
        if l.get('key_nb'):
            st.append(P('Notebook sample answers', 'h2'))
            st += render_blocks(l['key_nb'], CW)
    if unit.get('match'):
        st.append(PageBreak())
        st.append(P('Matching table: data to source of variation', 'h1'))
        st.append(P(esc(unit['match']['intro']), 'body'))
        st.append(Spacer(1, 5))
        st.append(blk_table(unit['match']['table'], CW))
    doc.build(st)


# ---------- HTML (Google Docs) ----------
def _h_table(b):
    out = ['<table border="1" cellpadding="4" style="border-collapse:collapse">']
    if b.get('header'):
        out.append('<tr>' + ''.join('<th>%s</th>' % c for c in b['header']) + '</tr>')
    for r in b['rows']:
        out.append('<tr>' + ''.join('<td>%s</td>' % (c or '&nbsp;') for c in r) + '</tr>')
    out.append('</table>')
    return ''.join(out)


def blocks_html(blocks):
    out = []
    for b in blocks:
        k = b[0]
        if k == 'p':
            out.append('<p>%s</p>' % b[1].replace('\n', '<br>'))
        elif k == 'h':
            out.append('<p><b>%s</b></p>' % b[1])
        elif k == 'note':
            out.append('<p><i>%s</i></p>' % b[1])
        elif k == 'table':
            out.append(_h_table(b[1]))
        elif k == 'cards':
            out.append('<p>Cards: ' + ' | '.join(b[1]) + '</p>')
        elif k == 'punnett':
            p = b[1]
            cells = p.get('cells') or [['', ''], ['', '']]
            out.append(_h_table({'header': [p.get('title', '')] + p['top'],
                                 'rows': [[p['side'][0]] + cells[0], [p['side'][1]] + cells[1]]}))
        elif k in ('lines', 'box', 'gap'):
            pass
    return '\n'.join(out)


def key_html(unit):
    h = ['<html><body>', '<h1>Unit %s Printables Teacher Key: %s</h1>' % (unit['id'], esc(unit['name'])),
         '<p>%s</p>' % esc(unit['std_line']), '<h2>Data caveats</h2><ul>']
    h += ['<li>%s</li>' % c for c in unit['caveats']]
    h.append('</ul>')
    for l in unit['lessons']:
        h.append('<h2>Lesson %d: %s</h2>' % (l['n'], esc(l['title'])))
        h.append('<p><i>Targets: %s</i></p>' % esc('; '.join(l['target_labels'])))
        for it in [i for i in unit['items'] if i['lesson'] == l['n']]:
            h.append('<h3>%s</h3>' % esc(it['title']))
            h.append(blocks_html(it['key']))
        if l.get('key_nb'):
            h.append('<h3>Notebook sample answers</h3>' + blocks_html(l['key_nb']))
    if unit.get('match'):
        h.append('<h2>Matching table: data to source of variation</h2><p>%s</p>' % esc(unit['match']['intro']))
        h.append(_h_table(unit['match']['table']))
    h.append('</body></html>')
    return '\n'.join(h)


def plan_html(unit, l, links=None):
    its = [i for i in unit['items'] if i['lesson'] == l['n']]
    h = ['<html><body>']
    h.append('<h1>Unit %s Lesson %d: %s</h1>' % (unit['id'], l['n'], esc(l['title'])))
    h.append('<p><i>Teacher plan · %s · %s</i></p>' % (esc(unit['name']), esc(unit['std_short'])))
    h.append('<h2>Focus question</h2><p>%s</p>' % esc(l['focus']))
    h.append('<h2>Learning target</h2><ul>' + ''.join('<li>%s</li>' % esc(t) for t in l['target_labels']) + '</ul>')
    h.append('<h2>Objective</h2><p>%s</p>' % esc(l['objective']))
    h.append('<h2>Agenda</h2><table border="1" cellpadding="4" style="border-collapse:collapse">'
             '<tr><th>Minutes</th><th>Segment</th><th>What students do</th></tr>' +
             ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (esc(a[0]), esc(a[1]), esc(a[2])) for a in l['agenda']) +
             '</table>')
    h.append('<h2>Materials and printables</h2><ul>')
    if its:
        for it in its:
            h.append('<li><b>%s</b> (%s). %s</li>' % (esc(it['title']), esc(it['copies']), esc(it['use'])))
    else:
        h.append('<li>No printable. Students use the slides and notebook.</li>')
    for m in l.get('materials', []):
        h.append('<li>%s</li>' % esc(m))
    h.append('</ul>')
    h.append('<h2>Notebook</h2><p>Pages: ________ (fill in from the student notebook). %s%s.</p>' %
             ('One reflection page' if not l['nb']['right'] else 'Left and right page for this lesson',
              ' plus a Part 2 reading spread' if l['nb'].get('part2') else ''))
    h.append('<h2>Teacher moves</h2><ul>' + ''.join('<li>%s</li>' % esc(t) for t in l['moves']) + '</ul>')
    h.append('<h2>Look-fors and common misconceptions</h2><ul>' + ''.join('<li>%s</li>' % esc(t) for t in l['misc']) + '</ul>')
    h.append('<h2>Check for understanding</h2><p>%s</p>' % esc(l['check']))
    h.append('<h2>If students are not there yet / extension</h2><p>%s</p>' % esc(l['diff']))
    h.append('<h2>Answer key</h2><p>Sample answers for this lesson are in the Unit %s Printables Teacher Key (lesson %d).</p>' % (unit['id'], l['n']))
    h.append('</body></html>')
    return '\n'.join(h)
