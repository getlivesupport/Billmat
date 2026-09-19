#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html")) + sorted((ROOT / "insurance-partners").glob("*.html"))


class TableWrapParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.bad_tables = 0

    def handle_starttag(self, tag, attrs):
        attrs_map = {k: v for (k, v) in attrs}
        classes = set((attrs_map.get("class") or "").split())
        self.stack.append((tag, classes))
        if tag == "table":
            if not any("table-wrap" in classes for _, classes in self.stack[:-1]):
                self.bad_tables += 1

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break


def fail(message):
    print(f"ERROR: {message}")
    return 1


def main():
    status = 0

    css = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
    if re.search(r"overflow-x\s*:\s*(hidden|clip)", css):
        status |= fail("css/style.css contains global overflow-x hiding/clipping.")

    for html_file in HTML_FILES:
        text = html_file.read_text(encoding="utf-8")

        if 'name="viewport"' not in text:
            status |= fail(f"{html_file.relative_to(ROOT)} is missing viewport metadata.")

        if "rel=\"preload\"" in text and "as=\"style\"" in text:
            status |= fail(f"{html_file.relative_to(ROOT)} still uses preload stylesheet pattern.")

        if not re.search(r'<link rel="stylesheet" href="(\.\./)?css/style\.css">', text):
            status |= fail(f"{html_file.relative_to(ROOT)} is missing stylesheet link to css/style.css.")

        parser = TableWrapParser()
        parser.feed(text)
        if parser.bad_tables:
            status |= fail(
                f"{html_file.relative_to(ROOT)} has {parser.bad_tables} table(s) outside .table-wrap."
            )

    if status == 0:
        print("Static site validation passed.")
    return status


if __name__ == "__main__":
    sys.exit(main())
