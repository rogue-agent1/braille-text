import sys, argparse

BRAILLE = {chr(i): chr(0x2800 + (i - ord("a") + 1)) for i in range(ord("a"), ord("z") + 1)}
BRAILLE.update({str(i): chr(0x2800 + i + 1) for i in range(10)})
BRAILLE[" "] = " "
REVERSE = {v: k for k, v in BRAILLE.items()}

def to_braille(text):
    return "".join(BRAILLE.get(c, c) for c in text.lower())

def from_braille(text):
    return "".join(REVERSE.get(c, c) for c in text)

def main():
    p = argparse.ArgumentParser(description="Text to Braille converter")
    p.add_argument("action", choices=["encode", "decode"])
    p.add_argument("text", nargs="?")
    args = p.parse_args()
    text = args.text or sys.stdin.read().strip()
    print(to_braille(text) if args.action == "encode" else from_braille(text))

if __name__ == "__main__":
    main()
