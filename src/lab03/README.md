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
