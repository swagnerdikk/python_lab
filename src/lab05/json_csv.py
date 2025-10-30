import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    if not json_path.endswith('.json'): 
        raise TypeError("Неверное расширение(only .json)")
    if not csv_path.endswith('.csv'):
        raise TypeError("Неверное расширение(olnly .csv)")

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            dannie = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    except json.JSONDecodeError as e:
        raise ValueError("Неверный формат оформления")
    

    if not isinstance(dannie, list):
        raise ValueError("JSON должен содержать список объектов")
    if len(dannie) == 0:
        raise ValueError("JSON-файл пуст")
    if not isinstance(dannie[0], dict):
        raise ValueError("Элементы списка должны быть словарями")
    
    zagolovki = list(dannie[0].keys())
    
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            isxod = csv.DictWriter(csv_file, fieldnames=zagolovki)
            isxod.writeheader()
            isxod.writerows(dannie)
    except IOError as e:
        raise IOError(f"Ошибка формата {e}")

json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    
    if not csv_path.endswith('.csv'):
        raise TypeError("Неверное расширение(only .csv)")
    if not json_path.endswith('.json'):
        raise TypeError("Неверное расширение(only .json)")
    
    rows = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)#читаем словари
            rows = list(reader)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
  
    if not rows:
        raise ValueError("CSV файл пуст")
    
    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, ensure_ascii=False, indent=2)
    except IOError as e:
        raise IOError(f"Ошибка формата {e}")


csv_to_json('data/lab05/samples/testik.csv', 'data/lab05/out/testik.json')