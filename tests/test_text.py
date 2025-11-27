import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


"""Базовые случаи"""


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


"""Пустая строка"""


def test_normalize_empty_string():
    assert normalize("") == ""


"""Только пробелы"""


def test_normalize_whitespace_only():
    assert normalize("   \t\n\r   ") == ""


"""Нормализация чисел"""


@pytest.mark.parametrize(
    "text, expected",
    [
        ("test123", "test123"),
        ("123test", "123test"),
        ("abc def", "abc def"),
    ],
)
def test_normalize_with_numbers(text, expected):
    assert normalize(text) == expected


"""Сохранение спецсимволов и пунктуации"""


def test_normalize_special_characters():
    assert normalize("hello, world!") == "hello, world!"
    assert normalize("test@email.com") == "test@email.com"


"""yo2e=False"""


def test_normalize_with_yo2e_false():
    assert normalize("ёжик", yo2e=False) == "ёжик"


"""casefold=False"""


def test_normalize_with_casefold_false():
    assert normalize("ПрИвЕт", casefold=False) == "ПрИвЕт"
    assert normalize("Hello", casefold=False) == "Hello"


"""Базовые случаи токенизации"""


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
    ],
)
def test_tokenize_basic(text, expected):
    assert tokenize(text) == expected


"""Пустая строка"""


def test_tokenize_empty_string():
    assert tokenize("") == []


"""Только знаки препинания"""


def test_tokenize_only_punctuation():
    assert tokenize("!@#$%^&*()") == []


"""Токенизация с подчеркиваниями"""


def test_tokenize_with_underscores():
    assert tokenize("hello_world test_case") == ["hello_world", "test_case"]


"""Множественные пробелы между словами"""


def test_tokenize_multiple_spaces():
    assert tokenize("hello     world") == ["hello", "world"]


"""Токенизация слов с дефисами"""


def test_tokenize_with_hyphens():
    assert tokenize("self-driving-car") == ["self-driving-car"]
    assert tokenize("-start middle- end-") == ["start", "middle-", "end-"]


"""Смешанные символы"""


def test_tokenize_mixed_content():
    assert tokenize("test123 hello456world") == ["test123", "hello456world"]


"""Перенос строк и табуляция"""


def test_tokenize_newlines_and_tabs():
    assert tokenize("hello\nworld\ttest") == ["hello", "world", "test"]


"""Базовый случай подсчета частот"""


def test_count_freq_basic():
    tokens = ["a", "b", "a", "c", "b", "a"]
    expected = {"a": 3, "b": 2, "c": 1}
    assert count_freq(tokens) == expected


"""Пустой список"""


def test_count_freq_empty_list():
    """Граничный случай: пустой список"""
    assert count_freq([]) == {}


"""Один токен"""


def test_count_freq_single_token():
    assert count_freq(["hello"]) == {"hello": 1}


"""Все токены одинаковые"""


def test_count_freq_all_same():
    tokens = ["test", "test", "test", "test"]
    assert count_freq(tokens) == {"test": 4}


"""Все токены уникальные"""


def test_count_freq_all_unique():
    tokens = ["a", "b", "c", "d", "e"]
    expected = {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1}
    assert count_freq(tokens) == expected


"""Подсчет частот с числами"""


def test_count_freq_with_numbers():
    tokens = ["123", "abc", "123", "abc", "123"]
    expected = {"123": 3, "abc": 2}
    assert count_freq(tokens) == expected


"""Базовый случай: топ-N по частоте"""


def test_top_n_basic():
    freq = {"apple": 5, "banana": 3, "cherry": 8, "date": 2}
    result = top_n(freq, n=2)
    assert result == [("cherry", 8), ("apple", 5), ("banana", 3), ("date", 2)]


"""Сортировка по алфавиту при одинаковой частоте"""


def test_top_n_tie_breaker():
    freq = {"bb": 2, "aa": 2, "cc": 3}
    result = top_n(freq, n=10)
    assert result == [("cc", 3), ("aa", 2), ("bb", 2)]


"""Пустой словарь"""


def test_top_n_empty_dict():
    assert top_n({}, n=5) == []


"""Один элемент в словаре"""


def test_top_n_single_item():
    assert top_n({"test": 10}, n=5) == [("test", 10)]


"""Все элементы с одинаковой частотой"""


def test_top_n_all_same_frequency():
    freq = {"dog": 1, "cat": 1, "bird": 1, "ant": 1}
    result = top_n(freq, n=10)
    assert result == [("ant", 1), ("bird", 1), ("cat", 1), ("dog", 1)]


"""Когда n больше количества элементов"""


def test_top_n_returns_all_when_n_larger():
    freq = {"a": 1, "b": 2}
    result = top_n(freq, n=100)
    assert len(result) == 2
    assert result == [("b", 2), ("a", 1)]


"""Смесь частот и алфавита"""


def test_top_n_complex_sorting():
    freq = {"z": 5, "a": 5, "m": 5, "b": 3, "y": 3, "c": 1}
    result = top_n(freq, n=10)
    assert result == [("a", 5), ("m", 5), ("z", 5), ("b", 3), ("y", 3), ("c", 1)]
