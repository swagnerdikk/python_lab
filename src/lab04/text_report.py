import csv
from collections import Counter
from pathlib import Path
import os, sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import tokenize, normalize, top_n, count_freq



def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читаем текст из файла 
    + обрабатваем несущестыующий файл
    """
    try:
        p = Path(path)
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        print('Файл не существует')
        sys.exit(-1)


nova_str = read_text("data/lab04/input.txt")


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens) 

def sorted_word(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))

def report_csv(word_counts: list[tuple[str, int]], path: str | Path = "report.csv") -> None:
    """
    Создаем отчет csv файлом
    word_counts: список кортежей 
    path: путь, по которому будет сохраняться отчет csv 
    """
    p = Path(path)
    with p.open("w", newline='', encoding="utf-8") as f:
        l = csv.writer(f)
        l.writerow(("word", "count"))
        for word, count in word_counts:
            l.writerow((word, count))

sorted_list = sorted_word(frequencies_from_text(nova_str))

report_csv(sorted_list, "data/lab04/report.csv")

print(f'Всего слов: {len((nova_str).split())}')
print(f'Уникальных слов: {len(set(tokenize(nova_str)))}')
print(f'Топ-5:')
for word, count in top_n(Counter(tokenize(nova_str)), 5):
    print(f'{word}:{count}')

print(f"Отчет выполнен и сохранен: data/lab04/report.csv")