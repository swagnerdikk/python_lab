import sys
import os
from pathlib import Path

lib_path = Path(__file__).parent.parent / "lib"
sys.path.insert(0, str(lib_path))

from lib.text import tokenize, normalize, count_freq, top_n


def read_stdin() -> str:
    return sys.stdin.read()


def stats(colvo_slov: int, unik_slova: int, top_items):
    print(f"Всего слов: {colvo_slov}")
    print(f"Уникальных слов: {unik_slova}")
    print("Топ-5:")
    for word, count in top_items:
        print(f"{word}:{count}")


def main():
    text = read_stdin()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq_map = count_freq(tokens)
    top = top_n(freq_map, 5)
    stats(len(tokens), len(set(tokens)), top)


if __name__ == "__main__":
    main()
