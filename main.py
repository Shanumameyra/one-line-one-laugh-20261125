"""One Line, One Laugh — make.fun entry.

Writes a single funny line of text to /output/entry.txt.
Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
"""

import os

LINE = "I went on a silent retreat and came back with strong opinions about everyone's breathing."


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line must be 1-140 characters, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
