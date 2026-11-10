import codecs
import re
from pathlib import Path


def read_log(path):
    raw = path.read_bytes()
    if raw.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig")


def evaluate(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    # Count whitespace-separated words, excluding bullet markers.
    words = sum(
        len(re.sub(r"^-\s+", "", line).split())
        for line in lines
    )
    three_bullets = (
        len(lines) == 3
        and all(line.startswith("- ") and line[2:].strip() for line in lines)
    )
    return words, three_bullets, words < 80


for filename in ("first-run.txt", "second-run.txt"):
    path = Path(filename)
    if not path.exists():
        print(f"\nMissing: {filename}")
        continue

    text = read_log(path)
    sections = re.findall(
        r"^=== (.*?) ===\s*\n(.*?)^Elapsed:\s*[\d.]+ seconds",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if len(sections) != 3:
        raise SystemExit(f"Expected three completed sections in {filename}.")

    print(f"\n=== {filename} ===")
    for label, answer in sections:
        words, bullets, short = evaluate(answer)
        if label == "Baseline":
            print(f"{label}: words={words}; format checks=N/A")
            continue
        status = "PASS" if bullets and short else "FAIL"
        print(
            f"{label}: {status}; words={words}; "
            f"three_bullets={bullets}; under_80={short}"
        )

print("\nThese checks assess format only, not factual accuracy or grounding.")
