import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY = os.path.join(OUT_DIR, "entry.txt")
TEXT = "Twelve yoghurts, no spoon, no plan. I have scanned your whole week, and honestly, the unexpected item is you."

os.makedirs(OUT_DIR, exist_ok=True)
with open(ENTRY, "w", encoding="utf-8") as stream:
    stream.write(TEXT + "\n")
