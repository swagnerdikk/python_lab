from openpyxl import Workbook
import csv

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    new_file = Workbook()
    listt = new_file.active
    listt.title = "1"
    
    with open(csv_path, encoding="utf-8") as f:
        for row in csv.reader(f):
                listt.append(row)
        for column in listt.columns:
            mx = 0
            column_letter = column[0].column_letter
            for cell in column:
                mx = max(mx, len(cell.value))
            new_width = max(mx + 2, 8)
            listt.column_dimensions[column_letter].width = new_width
    
    new_file.save(xlsx_path)
csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')  