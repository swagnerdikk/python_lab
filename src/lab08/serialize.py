import json
import sys
from pathlib import Path
from typing import List

try:
    from .models import Student
except (ImportError, ValueError):
    
    project_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(project_root))
    from src.lab08.models import Student


def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON файл.
    """
    data = [s.to_dict() for s in students]
    
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        raise IOError(f"Ошибка при записи файла: {e}")


def students_from_json(path: str) -> List[Student]:
    """
    Читает JSON-массив, валидирует данные и создаёт список Student.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Неверный формат JSON: {e}")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    students = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} должен быть словарём")
            
        try:
            student = Student.from_dict(item)
            students.append(student)
        except (KeyError, ValueError) as e:
            raise ValueError(f"Ошибка при создании Student из элемента {i}: {e}")
    
    return students


if __name__ == "__main__":

    from pathlib import Path
    
    project_root = Path(__file__).parent.parent.parent
    input_path = project_root / "data" / "lab08" / "students_input.json"
    output_path = project_root / "data" / "lab08" / "students_output.json"
    
    students = students_from_json(str(input_path))
    
    for student in students:
        print(f"• {student}")
    
    students_to_json(students, str(output_path))

   

