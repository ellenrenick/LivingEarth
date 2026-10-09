"""Print an update_presentation call one request per line (for reading and pasting)."""
import json, sys
c = json.load(open(sys.argv[1]))
print('{"requests":[')
for i, r in enumerate(c["requests"]):
    print(json.dumps(r, separators=(",", ":")) + ("," if i < len(c["requests"]) - 1 else ""))
print('],"writeControl":' + json.dumps(c["writeControl"], separators=(",", ":")) + "}")
