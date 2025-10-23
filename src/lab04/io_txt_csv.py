from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читаем текст из файлов в одну строку 
    Чтобы выбрать другую кодировку, просто меняем значение аргумента функции: 
    read_text("...", "cp1251") - заменили utf-8 на cp1251
    """
    p = Path(path)
    return p.read_text(encoding=encoding)
# если нужно убрать личшние пробелы return ''.join(p.read_text(encoding=encoding).split())
# print(read_text("data/lab04/input.txt"))
# print('*'*18)
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Создаем или перезаписываем csv
    + проверка длины строк на входе 
    """
    p = Path(path)
    rows = list(rows)
    for i in range(len(rows) - 1): 
        if len(rows[i]) != len(rows[i + 1]): raise ValueError
    with p.open("w", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None: w.writerow(header)
        for r in rows: w.writerow(r)
# write_csv([("word","count"),("test",3)], "data/lab04/check.csv", 'ddg') 
# write_csv(rows=[], path="data/lab04/check.csv", header=None)
write_csv(rows=[], path="data/lab04/check.csv", header='F')