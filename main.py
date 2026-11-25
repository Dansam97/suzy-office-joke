import os

ENTRY = "I blocked 'focus time' on my calendar, so my coworkers booked a meeting to ask what I focus on."

MAX_CHARS = 200


def render():
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(render() + "\n")

if __name__ == "__main__":
    main()
