from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """Валидация формата даты и диапазона gpa"""
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверный формат даты")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должен быть от 0 до 5")

    def age(self) -> int:
        """Возвращает количество полных лет студента"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        
        """Проверка на др в этом году"""
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        
        return age

    def to_dict(self) -> dict:
        """Сериализация объекта Student в словарь"""

        name_parts = self.fio.strip().split()
        name_surname = " ".join(name_parts[:2]) if len(name_parts) >= 2 else self.fio
        
        return {
            "fio": name_surname,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        """Десериализация словаря в объект Student"""
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
        """Красивый вывод информации о студенте"""
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}, Возраст: {self.age()} лет"


if __name__ == "__main__":
    student = Student(
        fio="Виноградов Антон Зумерович",
        birthdate="2006-05-15",
        group="BBIT-06-1",
        gpa=4.5
    )
    print(student)
    print(f"Словарь: {student.to_dict()}")
