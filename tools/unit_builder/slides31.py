import json, sys
from unit31 import unit, T
S = 'nbspread'
def sec_line(s):
    label, hint, h, kind = s
    h2 = hint.replace('Glue in: ', '')
    if kind == 'glue': return 'GLUE: ' + h2
    if kind == 'box': return 'SKETCH: ' + label
    return 'WRITE: ' + label
def page_text(side, focus, warm, secs, exit_):
    lines = [side + ' PAGE', 'Focus question: ' + focus]
    if warm: lines.append('Warm-up: ' + warm[1])
    lines += ['• ' + sec_line(s) for s in secs]
    if exit_: lines.append('Exit ticket: ' + exit_[1])
    return '\n'.join(lines)
def shape(id, x, y, w, h, kind='TEXT_BOX'):
    return {'createShape': {'objectId': id, 'shapeType': kind, 'elementProperties': {'pageObjectId': S,
            'size': {'width': {'magnitude': w, 'unit': 'PT'}, 'height': {'magnitude': h, 'unit': 'PT'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x, 'translateY': y, 'unit': 'PT'}}}}
def txt(id, t): return {'insertText': {'objectId': id, 'text': t}}
def sty(id, size, bold=False, start=None, end=None):
    r = {'updateTextStyle': {'objectId': id, 'style': {'fontSize': {'magnitude': size, 'unit': 'PT'}, 'bold': bold}, 'fields': 'fontSize,bold'}}
    if start is not None: r['updateTextStyle']['textRange'] = {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': end}
    else: r['updateTextStyle']['textRange'] = {'type': 'ALL'}
    return r
def box_fmt(id):
    return {'updateShapeProperties': {'objectId': id, 'fields': 'shapeBackgroundFill.solidFill.color,outline.outlineFill.solidFill.color,outline.weight',
            'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}},
                                'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': {'red': 0.2, 'green': 0.2, 'blue': 0.2}}}}, 'weight': {'magnitude': 1.25, 'unit': 'PT'}}}}}
def build(n, has_setup_slide=True, delete_ids=('slide06',), cer_note=True):
    l = [x for x in unit['lessons'] if x['n'] == n][0]
    nb = l['nb']
    rq = []
    rq.append({'createSlide': {'objectId': S, 'insertionIndex': 1, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}})
    rq += [shape(S+'_t', 24, 10, 672, 30), shape(S+'_l', 24, 46, 330, 300, 'RECTANGLE'), shape(S+'_r', 366, 46, 330, 300, 'RECTANGLE'), shape(S+'_f', 24, 352, 672, 40)]
    title = 'Lesson %d: %s · Notebook set-up' % (n, l['title'])
    left = page_text('LEFT', l['focus'], l['warmup'], nb['left'], None)
    right_secs = nb['right']
    right = page_text('RIGHT', l['focus'], None, right_secs, l['exit']) if right_secs else None
    if right is None:
        left = page_text('REFLECTION', l['focus'], l['warmup'], nb['left'], l['exit'])
    foot = 'Notebook pages: ________ (left)   ________ (right)' if right else 'Notebook page: ________'
    if nb.get('part2'): foot += '   ·   Part 2 reading spread: ________ (left)   ________ (right)'
    if cer_note: foot += '\nKeep your Unit CER evidence log (Evidence | Kind | What it shows) in the back of your notebook.'
    rq += [txt(S+'_t', title), sty(S+'_t', 18, True)]
    rq += [box_fmt(S+'_l'), txt(S+'_l', left), sty(S+'_l', 9), sty(S+'_l', 10, True, 0, left.index('\n'))]
    if right:
        rq += [box_fmt(S+'_r'), txt(S+'_r', right), sty(S+'_r', 9), sty(S+'_r', 10, True, 0, right.index('\n'))]
    else:
        rq.append({'deleteObject': {'objectId': S+'_r'}})
    rq += [txt(S+'_f', foot), sty(S+'_f', 10)]
    # targets slide
    tl = l['tl']
    lines = {k: T[k].replace(': ', '  ', 1) for k in T}
    sent = {k: T[k].split(': ', 1)[1] for k in T}
    if len(tl) == 1:
        k = tl[0]
        before = ''.join(lines[j] + '\n' for j in range(1, k))
        after = ''.join('\n' + lines[j] for j in range(k + 1, 7))
        cur = lines[k] + '\n'
        if before: rq.append({'insertText': {'objectId': 'sl04b', 'insertionIndex': 0, 'text': before}})
        if after: rq.append({'insertText': {'objectId': 'sl04b', 'insertionIndex': len(before) + len(lines[k]), 'text': after}})
    for k in tl:
        rq.append({'replaceAllText': {'containsText': {'text': sent[k], 'matchCase': True}, 'replaceText': sent[k] + ' ◀ TODAY', 'pageObjectIds': ['slide04']}})
    rq.append({'updateSlidesPosition': {'slideObjectIds': ['slide04'], 'insertionIndex': 2}})
    for d in delete_ids: rq.append({'deleteObject': {'objectId': d}})
    # notebook pages on title slide
    rq.append({'createShape': {'objectId': 'sl01_nbp', 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': 'slide01',
              'size': {'width': {'magnitude': 400, 'unit': 'PT'}, 'height': {'magnitude': 24, 'unit': 'PT'}},
              'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 24, 'translateY': 360, 'unit': 'PT'}}}})
    rq += [txt('sl01_nbp', 'Notebook pages: ________'), sty('sl01_nbp', 12)]
    rq.append({'replaceAllText': {'containsText': {'text': 'Day %d:' % n, 'matchCase': True}, 'replaceText': 'Lesson %d:' % n, 'pageObjectIds': ['slide01']}})
    return rq
if __name__ == '__main__':
    n = int(sys.argv[1])
    kw = {}
    if n == 10: kw = dict(delete_ids=(), cer_note=False)
    if n >= 9: kw['cer_note'] = False
    print(json.dumps(build(n, **kw), ensure_ascii=False, separators=(',', ':')))
