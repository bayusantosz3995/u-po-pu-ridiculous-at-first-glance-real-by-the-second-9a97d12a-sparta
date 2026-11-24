"""Entry for make.fun's "Ridiculous at First Glance, Real by the Second".

One sentence (<= 200 chars) pitching a startup so strange it sounds like
a joke, yet specific enough that the customers and the money are visible:
a company that rents out trained goats to mow lawns and clear brush.
Homeowners pay $49 per goat per day against a landscaper's $98; the goats
eat the weeds as they go, demand is proven (200 goats booked out every
weekend), and each goat arrives named, badged, and rated five stars -- the odd
detail that makes the $49-versus-$98 arithmetic feel like a real service.
"""

import os
import sys

TEXT = (
    "GoatCrew rents out trained goats at $49 a day: homeowners skip the "
    "mower, the goats eat the weeds, and 200 named, badged, five-star goats "
    "book out every weekend while landscapers charge $98."
)


def main() -> int:
    line = TEXT.strip()
    if not line:
        print("gate failed: empty entry", file=sys.stderr)
        return 1
    if "\n" in line:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(
            f"gate failed: entry is {len(line)} chars, over the 200-char limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
