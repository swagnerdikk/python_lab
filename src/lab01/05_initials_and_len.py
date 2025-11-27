fio = input("ФИО: ")
fio = fio.replace(" ", "")
iniciali = ""
for i in range(len(fio)):
    bukva = fio[i]
    if bukva.isupper():
        iniciali += bukva
    else:
        continue
print(f"Инициалы: {iniciali}.")
print(f"Длина (символов): {len(fio)+2}")
