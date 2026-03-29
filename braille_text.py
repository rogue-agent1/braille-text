#!/usr/bin/env python3
"""Braille Text - Convert text to Unicode Braille patterns."""
import sys

BRAILLE = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑", "f": "⠋", "g": "⠛",
    "h": "⠓", "i": "⠊", "j": "⠚", "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝",
    "o": "⠕", "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞", "u": "⠥",
    "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽", "z": "⠵",
    "1": "⠁", "2": "⠃", "3": "⠉", "4": "⠙", "5": "⠑",
    "6": "⠋", "7": "⠛", "8": "⠓", "9": "⠊", "0": "⠚",
    " ": "⠀", ".": "⠲", ",": "⠂", "!": "⠖", "?": "⠦", "'": "⠄", "-": "⠤",
}

REVERSE = {v: k for k, v in BRAILLE.items() if k.isalpha()}

def to_braille(text):
    return "".join(BRAILLE.get(c.lower(), c) for c in text)

def from_braille(braille):
    return "".join(REVERSE.get(c, c) for c in braille)

def braille_art(text, width=40):
    dots = [0x2800 + i for i in range(256)]
    result = to_braille(text)
    lines = [result[i:i+width] for i in range(0, len(result), width)]
    return "\n".join(lines)

def main():
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "hello world"
    print(f"=== Braille Converter ===\n")
    print(f"Text:    {text}")
    print(f"Braille: {to_braille(text)}")
    print(f"Back:    {from_braille(to_braille(text))}")
    print(f"\nAlphabet:")
    for c in "abcdefghijklmnopqrstuvwxyz":
        print(f"  {c} = {BRAILLE[c]}", end="")
        if (ord(c) - ord('a') + 1) % 9 == 0: print()
    print()

if __name__ == "__main__":
    main()
