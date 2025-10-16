#  Лр 3 
## normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str

Нормализует текст:
Приведение к нижнему регистру
Замена «ё» на «е»
Удаление лишних пробелов и переводов строк

![norm](/images/lab03/normalize.png)

## tokenize(text: str) -> list[str]

Разбивает текст на токены:
Поддерживает буквы, цифры и подчёркивание
Сохраняет дефисы внутри слов
Игнорирует знаки пунктуации и эмодзи

![token](/images/lab03/token.png)

## count_freq(tokens: list[str]) -> dict[str, int]

Подсчитывает частоту встречаемости каждого токена

![count_token](/images/lab03/count_token.png)

## top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]

Возвращает топ-N самых частых слов, отсортированных по убыванию частоты и алфавиту

![top_n](/images/lab03/top_n.png)

## Part 2 
Используя функции из задания №1, выполним задание №2

``` python 
import sys
import os
from pathlib import Path

lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from text import tokenize, normalize, count_freq, top_n


def read_stdin() -> str:
    return sys.stdin.read()


def stats(colvo_slov: int, unik_slova: int, top_items):
    print(f'Всего слов: {colvo_slov}')
    print(f'Уникальных слов: {unik_slova}')
    print('Топ-5:')
    for word, count in top_items:
        print(f'{word}:{count}')


def main():
    text = read_stdin()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq_map = count_freq(tokens)
    top = top_n(freq_map, 5)
    stats(len(tokens), len(set(tokens)), top)


if __name__ == '__main__':
    main()
```
![part2](/images/lab03/text_stats.png)

## read_stdin() -> str
Cчитывает строку с консоли 

## stats(colvo_slov: int, unik_slova: int, top_items)
Выводит параметры 

## main
Содержит функции, которые обрабатывают строчку, и вызывает stats 