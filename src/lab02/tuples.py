def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        raise ValueError  # Отсутствуют элементы
    fio, group, gpa = rec
    if group == "" or gpa > 5 or gpa < 0 or fio == "":
        raise ValueError  # Неверные данные(0<gpa<5)
    if (
        not isinstance(gpa, (int, float))
        or not isinstance(group, str)
        or not isinstance(fio, str)
    ):
        raise TypeError  # Неверный тип данных
    stroka = ""
    inic = fio.strip().split()
    if len(inic) == 3:
        inic = str(
            inic[0][0].upper()
            + inic[0][1::]
            + " "
            + (inic[1])[:1:].upper()
            + "."
            + (inic[2])[:1:].upper()
            + "."
        )
    else:
        inic = str(inic[0][0].upper() + inic[0][1::] + " " + (inic[1])[:1:] + ".")
    grupa = rec[1]
    ball = f"{gpa:.2f}"
    stroka = inic + ", гр. " + grupa + ", GPA " + ball
    return stroka


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", 5, 4.0)))
print("#" * 18)
