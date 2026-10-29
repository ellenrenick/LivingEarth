import json, sys
CANON = [('5.1', 'ESS1-5.1 (priority): I can describe Earth\'s outer layer as moving plates, name three kinds of plate boundaries, and describe where ocean crust is made and where it sinks back down.'),
         ('5.2', 'ESS1-5.2 (priority): I can read a rock-age map and describe the pattern in the ages.'),
         ('5.3', 'ESS1-5.3 (priority): I can explain why ocean crust is young and why continents are oldest at their ancient cores.'),
         ('5.4', 'ESS1-5.4 (priority): I can judge how strong the evidence is that the crust has moved and is still moving.'),
         ('5.5', 'ESS1-5.5 (priority): I can judge how well plate tectonics explains the ages of rocks, using evidence.'),
         ('6.1', 'ESS1-6.1 (supporting): I can list the evidence scientists use to learn about early Earth.'),
         ('6.2', 'ESS1-6.2 (supporting): I can explain why meteorites and moon rocks tell Earth\'s age better than Earth rocks do.'),
         ('6.3', 'ESS1-6.3 (supporting): I can use evidence from rocks, meteorites, and other planets to tell how Earth formed.')]
def R(old, new, page=None):
    d = {'replaceAllText': {'containsText': {'text': old, 'matchCase': True}, 'replaceText': new}}
    if page: d['replaceAllText']['pageObjectIds'] = [page]
    return d
def D(i): return {'deleteObject': {'objectId': i}}
def CELL(t, r, c, text):
    return [{'deleteText': {'objectId': t, 'cellLocation': {'rowIndex': r, 'columnIndex': c}, 'textRange': {'type': 'ALL'}}},
            {'insertText': {'objectId': t, 'cellLocation': {'rowIndex': r, 'columnIndex': c}, 'text': text}}]
def PLAN(t, rows):
    out = []
    for i, (m, p) in enumerate(rows, start=1):
        out += CELL(t, i, 0, m) + CELL(t, i, 1, p)
    return out
def LT(deck_k, today):
    lines = []
    for code, s in CANON:
        lines.append(s + (' ◀ TODAY' if code in today else ''))
    return [{'deleteText': {'objectId': 'v3l%d_lt_list' % deck_k, 'textRange': {'type': 'ALL'}}},
            {'insertText': {'objectId': 'v3l%d_lt_list' % deck_k, 'text': '\n'.join(lines)}}]
def NEWSLIDE(idx, sid, kick, title, body):
    def box(i, x, y, w, h): return {'createShape': {'objectId': sid + i, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': sid,
        'size': {'width': {'magnitude': w, 'unit': 'PT'}, 'height': {'magnitude': h, 'unit': 'PT'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x, 'translateY': y, 'unit': 'PT'}}}}
    def st(i, size, bold): return {'updateTextStyle': {'objectId': sid + i, 'style': {'fontSize': {'magnitude': size, 'unit': 'PT'}, 'bold': bold}, 'fields': 'fontSize,bold', 'textRange': {'type': 'ALL'}}}
    return [{'createSlide': {'objectId': sid, 'insertionIndex': idx, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
            box('_k', 36, 24, 648, 20), box('_t', 36, 48, 648, 44), box('_b', 36, 104, 648, 270),
            {'insertText': {'objectId': sid + '_k', 'text': kick}}, st('_k', 11, True),
            {'insertText': {'objectId': sid + '_t', 'text': title}}, st('_t', 26, True),
            {'insertText': {'objectId': sid + '_b', 'text': body}}, st('_b', 16, False)]
def NB(k, oldday, oldtitle, newn, newtitle):
    return [R('Day %d: %s Notebook Setup' % (oldday, oldtitle), 'Lesson %d: %s · Notebook set-up' % (newn, newtitle))]
def common(k, newn, oldtitle, newtitle=None, oldfocus=None, newfocus=None):
    r = [R('LESSON %d' % k, 'LESSON %d' % newn, 'v2l%d_s1' % k), R('Lesson %d ·' % k, 'Lesson %d ·' % newn)]
    if newtitle: r.append(R(oldtitle, newtitle))
    if oldfocus: r.append(R(oldfocus, newfocus))
    return r
decks = {}
# ---- N1 launch (E1)
def n1():
    r = common(1, 1, '', None)
    r.append(R('Focus question: How old is the ocean floor compared with the continents, and how do moving plates make and destroy it?', 'Focus question: Why is the seafloor so much younger than the continents?'))
    r += [D('a1_s9'), D('a1_s10'), D('a1_s11'), D('a1_s12'), D('a1_s13')]
    r += PLAN('a1s2plan', [('8', 'Hook: the mystery'), ('13', 'Lab A: plot the pattern'), ('19', 'Pre-check, first claim, and preview of the targets'), ('5', 'Wrap-up and exit ticket')])
    r += [R('compare the ages of the ocean floor and the continents', 'compare the ages of the ocean floor and the continents', 'a1_s2'),
          R('name three plate boundaries and what plates do at each', 'find a pattern in where earthquakes and volcanoes happen', 'a1_s2'),
          R('say where ocean crust is made and where it sinks', 'make a first claim and preview the unit targets', 'a1_s2')]
    r += [R('Where is ocean crust made, and where does it sink back down? Add the words ridge and trench to your first claim if they help.', 'Write what the dots on your map show about where earthquakes and volcanoes happen. Add the word plate to your first claim if it helps.'),
          R('Where is ocean crust made, and where does it sink back down?', 'What pattern do the dots on your map make?'),
          R('Finish by Day 7.', 'Finish all 8 by Lesson 9.')]
    r += [D('nbk1r2h'), D('nbk1r2b')] + NB(1, 1, 'Where Did the Old Ocean Floor Go?', 1, 'Where Did the Old Ocean Floor Go?')
    r += NEWSLIDE(10, 'nd1pre', 'PRE-ASSESSMENT · 5 MIN · ON YOUR OWN', 'Pre-check (not graded)', 'Glue in the pre-check under "Pre-check" in your notebook. Answer all five questions. It is OK to guess.\nWe will come back to these at the end of the unit.')
    r += NEWSLIDE(11, 'nd1prev', 'PREVIEW THE UNIT · 5 MIN', 'What you will learn', 'Read the five priority targets (and the three early-Earth targets). Put a star next to the one you think will be hardest.\nThe unit answers: Why is the seafloor so much younger than the continents?')
    r += LT(1, ['5.1', '5.2', '5.3', '5.4', '5.5'])
    return r
decks['N1'] = ('1jixcrdlU3A_OuouXzGiX6Up9j2O_wfcIiNXWSfa0cTw', n1)
# ---- N2 (copy of E1)
def n2():
    r = [R('LESSON 1', 'LESSON 2', 'v2l1_s1'), R('Lesson 1 ·', 'Lesson 2 ·'),
         R('Where Did the Old Ocean Floor Go?', 'Three Ways Plates Meet'),
         R('Focus question: How old is the ocean floor compared with the continents, and how do moving plates make and destroy it?', 'Focus question: What happens where plates meet, and where is ocean crust made and destroyed?'),
         R('Focus question: Why is the seafloor so much younger than the continents?', 'Focus question: What happens where plates meet, and where is ocean crust made and destroyed?')]
    r += [D('a1_s3'), D('a1_s4'), D('a1_s5'), D('a1_s6'), D('a1_s7'), D('a1_s8')]
    r += PLAN('a1s2plan', [('8', 'Warm-up: the map pattern'), ('10', 'Reading notes: Lesson 8.1, first chunk (pp. 206-218)'), ('17', 'Lab B: clay plate models'), ('10', 'Exit ticket and CFA ESS1-5.1')])
    r += [R('compare the ages of the ocean floor and the continents', 'recall the pattern from yesterday\'s map', 'a1_s2'), R('Finish by Day 7.', 'Finish all 8 by Lesson 9.')]
    r += [D('nbk1l1h'), D('nbk1l1b'), D('nbk1l3h'), D('nbk1l3b'), D('nbk1r1h'), D('nbk1r1b')]
    r += [R('Day 1: Three Ways Plates Meet Notebook Setup', 'Lesson 2: Three Ways Plates Meet · Notebook set-up'), R('Day 1: Where Did the Old Ocean Floor Go? Notebook Setup', 'Lesson 2: Three Ways Plates Meet · Notebook set-up')]
    r += NEWSLIDE(9, 'nd2cfa', 'START WITH A CFA · 8 MIN', 'CFA ESS1-5.1: Plates, boundaries, and crust', 'Take the CFA on Canvas now (5 questions).\nBelow 3 out of 4? A review for this target opens for you.')
    r += LT(1, ['5.1'])
    return r
decks['N2'] = ('1v19MNB0fSRtQdQ0ZkMX9U-_GEypUtP7K0Uzo3dtfivQ', n2)

def n3():
    r = common(2, 3, '') + NB(2, 2, 'Reading Rock Ages', 3, 'Reading Rock Ages')
    r += [D('a2_s3')]
    r += PLAN('a2s2plan', [('3', 'Warm-up: which rock is older?'), ('3', 'Reading notes: Lesson 8.1 (continued)'), ('12', 'Lab A: color the seafloor'), ('9', 'Lab B: graph the pattern'), ('8', 'Lab C: color North America'), ('10', 'Wrap-up and CFA ESS1-5.2')])
    r += [R('Tomorrow starts with CFA ESS1-5.2: Reading rock ages. Study your colored boxes and graph.', 'Then take CFA ESS1-5.2 on Canvas now (5 questions). Below 3 out of 4? A review for this target opens for you.'), R('WRAP-UP \u00b7 3 MIN', 'WRAP-UP AND CFA \u00b7 10 MIN', 'a2_s12')]
    r += LT(2, ['5.2'])
    return r
decks['N3'] = ('1HSXSeBpKhiUkV4tI-e9IYofiY4CcY9aaCLQh4QxrXZw', n3)
def n5():
    r = common(3, 5, 'Reading Deep Time and Early Earth', 'Meteorites and Moon Rocks',
               'Focus question: How do scientists know how old Earth is, and why do meteorites and moon rocks tell Earth\'s age better than Earth rocks do?', 'Focus question: Why do meteorites and moon rocks tell Earth\'s age better than Earth rocks do?')
    r += [R('Day 3: Meteorites and Moon Rocks Notebook Setup', 'Lesson 5: Meteorites and Moon Rocks \u00b7 Notebook set-up'),
          R('Focus question: How do scientists know how old Earth is, and why use meteorites and moon rocks?', 'Focus question: Why do meteorites and moon rocks tell Earth\'s age better than Earth rocks do?'),
          R('45 cm Earth timeline', 'Half-life model'), R(': timeline table and old materials. Tape your 45 cm strip below.', ': half-life decay record and graph.')]
    r += [D('a3_s3'), D('a3_s7'), D('a3_s8'), D('a3_s9')]
    r += PLAN('a3s2plan', [('3', 'Warm-up'), ('5', 'Hook and key ideas'), ('15', 'Simulation: crater counter'), ('12', 'Quick lab: half-life model'), ('10', 'How Earth formed and exit ticket')])
    r += NEWSLIDE(11, 'nd5half', 'QUICK LAB \u00b7 12 MIN \u00b7 WITH A PARTNER', 'Half-life model: pennies as atoms', '100 pennies in a shoebox. Shake, pour out, remove the heads (decayed), count what is left, and repeat six times.\nRecord each count and graph pennies left against shakes. Each shake is one half-life.\nGLUE IN: Half-life model: decay record.')
    r += NEWSLIDE(12, 'nd5form', 'HOW EARTH FORMED \u00b7 10 MIN', 'What meteorites and moon rocks tell us', 'Meteorites are leftovers from the solar system\'s formation: about 4.56 billion years old.\nMoon highlands rock is up to about 4.4 billion years old. The Moon has no plate tectonics, so its old rocks survive.\nEarth\'s oldest zircons (4.4 billion years) show solid crust soon after Earth formed.\nTogether: Earth formed about 4.5 billion years ago, and its earliest record was recycled.')
    r += LT(3, ['6.2', '6.3'])
    return r
decks['N5'] = ('16MMMNpyR7tWlrmX55qWjtO225xjjaN8IUAWu1jwQ734', n5)
def n4():
    r = [R('LESSON 3', 'LESSON 4', 'v2l3_s1'), R('Lesson 3 \u00b7', 'Lesson 4 \u00b7'),
         R('Reading Deep Time and Early Earth', 'Clues to Early Earth'),
         R('Focus question: How do scientists know how old Earth is, and why do meteorites and moon rocks tell Earth\'s age better than Earth rocks do?', 'Focus question: How do scientists learn about early Earth when the oldest ocean floor is only 200 million years old?'),
         R('Focus question: How do scientists know how old Earth is, and why use meteorites and moon rocks?', 'Focus question: How do scientists learn about early Earth when the oldest ocean floor is only 200 million years old?'),
         R('Day 3: Clues to Early Earth Notebook Setup', 'Lesson 4: Clues to Early Earth \u00b7 Notebook set-up'),
         R('impact crater', 'zircon'), R('Crater counts', 'Evidence list for early Earth'), R(': crater count table and three questions.', ': early Earth evidence log.')]
    r += [D('a3_s3'), D('a3sim0'), D('a3sim1'), D('a3sim2'), D('a3sim3'), D('a3sim4'), D('a3sim5')]
    r += PLAN('a3s2plan', [('3', 'Warm-up'), ('5', 'Hook and key ideas'), ('15', 'Lab B: Earth timeline'), ('14', 'Evidence list for early Earth'), ('8', 'Wrap-up and exit ticket')])
    r += [R('explain why meteorites and moon rocks give the age of the solar system', 'place the oldest evidence on a timeline of Earth', 'a3_s2'),
          R('Why do scientists use meteorites and moon rocks, not Earth rocks, to find the age of the solar system?', 'List two kinds of evidence scientists use to learn about early Earth, and say what each one shows.')]
    r += NEWSLIDE(8, 'nd4list', 'EVIDENCE LIST \u00b7 14 MIN \u00b7 WITH A PARTNER', 'What evidence do scientists use for early Earth?', 'Use your timeline and Lesson 8.2, Life\'s Early History (pp. 219-225).\nList each kind of evidence, where it is found, its age, and what it tells us.\nGLUE IN: Early Earth evidence log.')
    r += LT(3, ['6.1'])
    return r
decks['N4'] = ('1At1L8ndsPGjv2An2cBrHvQ4zwZBkXu6iWdCQKKhzA6M', n4)
def n6():
    r = common(4, 6, '') + [R('Day 4: Why the Ocean Is Young, the Continents Old Notebook Setup', 'Lesson 6: Why the Ocean Is Young and the Continents Old \u00b7 Notebook set-up')]
    r += PLAN('a4s2plan', [('3', 'Warm-up'), ('7', 'Guided notes'), ('15', 'Lab: sink or float'), ('12', 'SketchNotes'), ('8', 'Wrap-up and CFA ESS1-5.3')])
    r += [R('Tomorrow starts with CFA ESS1-5.3: Why ocean crust is young and continents are old.', 'Take CFA ESS1-5.3 on Canvas now (5 questions). Below 3 out of 4? A review for this target opens for you.'), R('Study your SketchNotes tonight.', 'Then study your SketchNotes tonight.'), R('WRAP-UP \u00b7 3 MIN', 'WRAP-UP AND CFA \u00b7 8 MIN', 'a4_s9')]
    r += LT(4, ['5.3'])
    return r
decks['N6'] = ('1VPyj3VZ8VJo4PMlwCkD32tKwfSlL0jef1GLMHbTsXKk', n6)
def n7():
    r = common(5, 7, '') + [R('Day 5: Evidence for Moving Crust Notebook Setup', 'Lesson 7: Evidence for Moving Crust \u00b7 Notebook set-up')]
    r += [D('a5_s3')]
    r += PLAN('a5s2plan', [('2', 'Day 1 warm-up'), ('12', 'Day 1 Lab A: magnetic stripes'), ('7', 'Day 1 Lab B: Hawaii and GPS'), ('3', 'Day 2 warm-up'), ('9', 'Day 2 Lab C: Pangaea puzzle'), ('14', 'Day 2 evaluate the evidence and CFA ESS1-5.4')])
    r += NEWSLIDE(8, 'nd7day2', 'DAY 2 \u00b7 WARM-UP \u00b7 3 MIN', 'Which lines of evidence have we used?', 'List the evidence you have so far that the crust moves (rock ages, magnetic stripes, Hawaii and GPS).\nToday you add fossils and judge how strong each line of evidence is.')
    r += NEWSLIDE(12, 'nd7cfa', 'CFA \u00b7 8 MIN \u00b7 END OF DAY 2', 'CFA ESS1-5.4: Evidence for moving crust', 'Take the CFA on Canvas now (5 questions).\nBelow 3 out of 4? A review for this target opens for you.')
    r += LT(5, ['5.4'])
    return r
decks['N7'] = ('1wIHGn3YxX2ck7dlbBs9APHyLddQZ9VOHpaNjqp1CgHs', n7)
def n8():
    r = common(6, 8, '') + [R('Day 6: Evaluate the Theory, Tell Earth\'s Story Notebook Setup', 'Lesson 8: Evaluate the Theory, Tell Earth\'s Story \u00b7 Notebook set-up')]
    r += [D('a6_s3')]
    r += PLAN('a6s2plan', [('3', 'Day 1: sort your evidence'), ('14', 'Day 1: Part A, evaluate the theory'), ('5', 'Day 1: peer feedback'), ('4', 'Day 2: revisit your Lesson 1 claim'), ('12', 'Day 2: Part B, Earth\'s story'), ('8', 'Day 2: wrap-up and CFA ESS1-5.5')])
    r += NEWSLIDE(9, 'nd8day2', 'DAY 2 \u00b7 WARM-UP \u00b7 4 MIN', 'Look back at your Lesson 1 claim', 'Reread your first claim about why the seafloor is younger than the continents.\nWrite one sentence: what would you change now, and which evidence changed your mind?')
    r += [R('Take it at the start of your next class or on the work day.', 'Take it now.'), R('WRAP-UP \u00b7 3 MIN', 'WRAP-UP AND CFA \u00b7 8 MIN', 'a6_s11')]
    r += LT(6, ['5.5', '6.3'])
    return r
decks['N8'] = ('1wOAy-mg3kiQ2id1XM4eczAyd7n44i1QfUpjKj6d7mbs', n8)
def n9():
    r = common(7, 9, '') + [R('Day 7: Review Day Notebook Setup', 'Lesson 9: Review Day \u00b7 Notebook set-up'), R('Have not taken a CFA yet? Take it now, including CFA ESS1-5.5.', 'Have not taken a CFA yet? Take it now.')]
    r += LT(7, ['5.1', '5.2', '5.3', '5.4', '5.5'])
    return r
decks['N9'] = ('16XlgCtVNTOkOv-AK35Qi0rsWUWMcx4lEkoiEvJb-o2U', n9)
def n10():
    r = common(8, 10, '')
    r += NEWSLIDE(1, 'nd10nb', 'NOTEBOOK SET-UP \u00b7 REFLECTION PAGE', 'Lesson 10: Unit 3.2 CSA \u00b7 Notebook set-up', 'Focus question: What do you know about the ages of Earth\'s crust?\nWarm-up: Before the CSA, I feel ____ about ____.\nWRITE: What I learned about the ages of Earth\'s crust (three things).\nWRITE: Where did the old ocean floor go? Explain it with plates, density, and evidence.\nExit ticket: The one idea I want to remember from this unit is ____.\nNotebook page: ________')
    r += LT(8, ['5.1', '5.2', '5.3', '5.4', '5.5'])
    return r
decks['N10'] = ('1kgF38spLmf92nAZOThJb8IJdnwW2tiLNXR7F1TCzyVY', n10)
if __name__ == '__main__':
    k = sys.argv[1]
    print(json.dumps(decks[k][1](), ensure_ascii=False, separators=(',', ':')))
