"""Build one self-contained review site per unit. Run: python3 build.py"""
import json
from pathlib import Path
from units import UNITS

HERE = Path(__file__).parent
css = (HERE / "engine.css").read_text()
js = (HERE / "engine.js").read_text()

for u in UNITS:
    data = json.dumps({k: u[k] for k in ("code", "eyebrow", "title", "lede", "footer", "ideas", "vocab", "vocabQuiz", "practice", "model", "rubric", "write", "ready")})
    data = data.replace("</", "<\\/")
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{u['page_title']}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap">
<style>
{css.replace('--accent:#1f5fbf;', '--accent:' + u['accent'] + ';', 1)}
</style>
</head>
<body>
<div class="wrap" id="app"></div>
<script>window.UNIT={data};</script>
<script>
{js}
</script>
</body>
</html>
"""
    out = HERE.parent / u["out"]
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)
    print("wrote", out, len(page))
