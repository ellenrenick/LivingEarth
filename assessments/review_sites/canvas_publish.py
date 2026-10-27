"""Upload the review sites to a Canvas course's Files and add them to a new module at the top.

Usage: CANVAS_TOKEN=... python3 canvas_publish.py https://kernhigh.instructure.com 330720
Everything is created unpublished. Running it again creates a second module.
"""
import json, os, ssl, sys, urllib.parse, urllib.request
from pathlib import Path
from units import UNITS

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
base, course = sys.argv[1].rstrip("/"), sys.argv[2]
tok = os.environ["CANVAS_TOKEN"]
ROOT = Path(__file__).parent.parent


def api(method, path, body=None, form=None):
    url = base + path
    data = json.dumps(body).encode() if body is not None else (urllib.parse.urlencode(form).encode() if form else None)
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {tok}")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, context=CTX) as r:
        return json.loads(r.read() or "null")


def upload(path):
    meta = api("POST", f"/api/v1/courses/{course}/files", form={
        "name": path.name, "size": path.stat().st_size, "content_type": "text/html",
        "parent_folder_path": "Review Sites", "on_duplicate": "overwrite"})
    boundary = "----rs" + os.urandom(8).hex()
    parts = []
    for k, v in meta["upload_params"].items():
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{path.name}"\r\nContent-Type: text/html\r\n\r\n'.encode() + path.read_bytes() + f"\r\n--{boundary}--\r\n".encode())
    req = urllib.request.Request(meta["upload_url"], data=b"".join(parts), method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k): return None
    opener = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=CTX))
    try:
        r = opener.open(req); loc = r.headers.get("Location"); body = r.read()
    except urllib.error.HTTPError as e:
        if e.code not in (301, 302, 303): raise
        loc = e.headers["Location"]; body = b""
    if loc:
        creq = urllib.request.Request(loc, method="GET"); creq.add_header("Authorization", f"Bearer {tok}")
        with urllib.request.urlopen(creq, context=CTX) as r: return json.loads(r.read())
    return json.loads(body)


mod = api("POST", f"/api/v1/courses/{course}/modules", body={"module": {"name": "Review Sites (Intervention before Reassessment)", "position": 1}})
print("module", mod["id"])
pos = 1
for u in UNITS:
    f = upload(ROOT / u["out"])
    print("file", f["id"], f["display_name"])
    api("POST", f"/api/v1/courses/{course}/modules/{mod['id']}/items", body={"module_item": {
        "title": u["eyebrow"].split(" · ")[0] + " Review Site: " + u["title"], "type": "File", "content_id": f["id"], "position": pos}})
    pos += 1
