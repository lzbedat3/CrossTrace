"""Build the Gantt page (site/index.html) from tasks.json and template.html.

Usage:  python3 gantt/build.py
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / "tasks.json").read_text(encoding="utf-8"))
template = (root / "template.html").read_text(encoding="utf-8")

out = root.parent / "site" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(template.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
print(f"Built {out.relative_to(root.parent)} ({len(data['tasks'])} items)")
