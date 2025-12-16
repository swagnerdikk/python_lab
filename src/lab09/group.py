import csv
from pathlib import Path
from typing import List
import sys

try:
    from src.lab08.models import Student
except (ImportError, ValueError):
    project_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(project_root))
    from src.lab08.models import Student


class Group:

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        '''Создание файла, если его нет '''
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Создаем файл с заголовком, если его ещё нет"""
        if not self.path.exists():
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                writer.writeheader()

    def _read_all(self) -> List[dict]:
        """
        Читаем все строки из CSV.
        """
        if not self.path.exists():
            return []
        
        rows = []
        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            """Если нет заголовка"""
            if reader.fieldnames != ["fio", "birthdate", "group", "gpa"]:
                raise ValueError("Неверный формат CSV: отсутствует или неверный заголовок")
            
            for row in reader:
                # Пропускаем пустые строки
                if any(row.values()):
                    # Конвертируем gpa в float
                    if "gpa" in row and row["gpa"]:
                        try:
                            row["gpa"] = float(row["gpa"])
                        except ValueError:
                            raise ValueError(f"Неверное значение gpa: {row['gpa']}")
                    rows.append(row)
        
        return rows

    def _write_all(self, rows: List[dict]):
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]:
        rows = self._read_all()
        students = []
        for i, row in enumerate(rows):
            try:
                student = Student.from_dict(row)
                students.append(student)
            except (KeyError, ValueError) as e:
                raise ValueError(f"Ошибка при создании Student из строки {i + 2}: {e}")
        return students

    def add(self, student: Student):
        rows = self._read_all()
        # Преобразуем Student в словарь и добавляем
        student_dict = student.to_dict()
        rows.append(student_dict)
        self._write_all(rows)

    def find(self, substr: str) -> List[Student]:
        """
        Найти студентов по подстроке в fio
        """
        rows = self._read_all()
        matching_rows = [r for r in rows if substr.lower() in r["fio"].lower()]
        
        students = []
        for row in matching_rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except (KeyError, ValueError) as e:
                raise ValueError(f"Ошибка при создании Student: {e}")
        
        return students

    def remove(self, fio: str):
        """
        Удалить запись(и) с данным fio.
        """
        rows = self._read_all()
        # Удаляем все записи с совпадающим fio
        rows = [r for r in rows if r["fio"] != fio]
        self._write_all(rows)

    def update(self, fio: str, **fields):
        """
        Обновить поля студента
        """
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row["fio"] == fio:
                for key, value in fields.items():
                    if key in ["fio", "birthdate", "group", "gpa"]:
                        # Конвертируем gpa в float, если передано как строка
                        if key == "gpa" and isinstance(value, str):
                            try:
                                value = float(value)
                            except ValueError:
                                raise ValueError(f"Неверное значение gpa: {value}")
                        row[key] = value
                    else:
                        raise ValueError(f"Неизвестное поле: {key}")
                try:
                    Student.from_dict(row)
                except (KeyError, ValueError) as e:
                    raise ValueError(f"Ошибка валидации обновлённых данных: {e}")
                
                updated = True
                break
        
        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(rows)


# if __name__ == '__main__':
    
#     #Создаём группу
#     group = Group('data/lab09/students.csv')
    
    # Проверяем начальное состояние
    # students = group.list()
    # for s in students:
    #     print(f"- {s}")
    
    # Добавляем студентов
    # students_to_add = [
    #     Student("Иванов Питер", "2003-10-10", "БИВТ-21-1", 4.3),
    #     Student("Петров Петр", "2002-05-20", "SE-01", 4.5),
    #     Student("Вмнокурова Анастасия", "2004-03-15", "БИВТ-21-1", 4.8),
    # ]
    
    # for student in students_to_add:
    #     group.add(student)
    
    # #Получаем список всех студентов
    # all_students = group.list()
    # for i, student in enumerate(all_students, 1):
    #     print(f"{i}. {student}")
    
    # Поиск студентов
    # found = group.find("Иванов")
    # for student in found:
    #     print(f"Найден: {student}")
    
    # #Обновление данных
    # group.update("Иванов Иван", gpa=4.9)
    # # Используем точный поиск по полному ФИО, а не по подстроке
    # updated_student = group.find("Иванов Иван")[0]
    # print(f"Обновлён: {updated_student}")
    
    # #Финальный список
    # final_students = group.list()
    # for i, student in enumerate(final_students, 1):
    #     print(f"{i}. {student}")
    
    # #Удаление студента
    # group.remove("Петров Петр")

    
    # #Список после удаления
    # remaining = group.list()
    # for i, student in enumerate(remaining, 1):
    #     print(f"{i}. {student}")
    

    