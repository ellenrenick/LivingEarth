"""Split a deck's request list into batches: front matter, one per content slide, and the closing delete+reorder."""
import json, sys
import slides
day = int(sys.argv[1]); out = sys.argv[2]
r, w = slides.deck(day)
dup = [i for i, x in enumerate(r) if 'duplicateObject' in x]
end = next(i for i, x in enumerate(r) if x.get('deleteObject', {}).get('objectId') == 'tpl_content')
cuts = [0] + dup + [end]
batches = [r[cuts[i]:cuts[i + 1]] for i in range(len(cuts) - 1)] + [r[end:]]
for k, b in enumerate(batches):
    open(f'{out}/d{day}_b{k}.json', 'w').write(json.dumps(b, ensure_ascii=False, separators=(',', ':')))
    print(k, len(json.dumps(b, separators=(',', ':'))))
