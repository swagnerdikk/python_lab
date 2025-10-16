# laboratoriti

# Лабораторная работа 1
## Задание 1
```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![name and age](./images/lab01/ex01.png)

## Задание 2 
```python
a = input('a: ')
b = input('b: ')
a = float(a.replace(',','.'))
b = float(b.replace(',','.'))
print(f'sum={a+b}; avg={((a+b)/2):.2f}')
```
![sum and avg](./images/lab01/ex02.png)

## Задание 3
```python
price = int(input('price='))
discount = int(input('discount='))
vat = int(input('vat='))
base = price * (1-discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:20.2f} ₽')
print(f'Итого к оплате: {total:10.2f} ₽')
```
![discount and vat](./images/lab01/ex03.png)

## Задание 4
```python
m = int(input('Минуты: '))
print(f'{m//60}:{m%60:02d}')
```
![minutes to hhmm](./images/lab01/ex04.png)

## Задание 5
```python
fio = input('ФИО: ')
fio = fio.replace(' ','')
iniciali = ''
for i in range(len(fio)):
    bukva = fio[i]
    if bukva.isupper():
        iniciali += bukva
    else:
        continue
print(f'Инициалы: {iniciali}.')
print(f'Длина (символов): {len(fio)+2}')
```
![initials and len](./images/lab01/ex05.png)

## Задание 6 
```python
kolich = int(input('in_1: '))
ochno_ = 0
zaochno_ = 0
for i in range(kolich):
    ychastnik = input(f'in_{i+2}: ')
    if 'True' in ychastnik:
        ochno_ = ochno_+1
    else:
        zaochno_ = zaochno_ +1
print(f'out: {ochno_} {zaochno_}')
```
![zvezdochka#6](./images/lab01/ex06.png)

## Задание 7
```python
vxod = input('in: ')
itog_ = ''
index_1 = 0 
index_2 = 0

for i in range(len(vxod)):
    if vxod[i].isupper():
        index_1 = i 
        break
    else:
        continue 
for i in range(len(vxod)):
    if vxod[i] in '0123456789':
        index_2 = i+1
        break
    else:
        continue
shag = index_2 - index_1
for i in range(index_1,len(vxod),shag):
    itog_+=vxod[i]
print(f'out: {itog_}')
```
![zvezdochka#7](./images/lab01/ex07.png)

# Лабораторная работа 2
## Задание 1
```python
ddef min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError
    return (min(nums), max(nums))
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print('#'*18)
print('')
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print('#'*18)
print('')
def flatten(mat: list[list | tuple]) -> list:
    res = []
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise ValueError
        if isinstance(row,(list,tuple)):
            res.extend(row)
    return res
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))  
print(flatten([[1], [], [2, 3]]))  
print(flatten([[1, 2], "ab"])) 
print('#'*18)
```
![arrays](./images/lab02/ex01.png)

## Задание 2
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    rvan = [len(x) for x in mat]
    if len(set(rvan))!=1:
        raise ValueError
    return [list(col) for col in zip(*mat)]
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print('#'*18)
print('')

def row_sums(mat: list[list[float | int]]) -> list[float]:
    rvan = [len(x) for x in mat]
    if len(set(rvan)) != 1:
        raise ValueError
    res = []
    for i in range(len(mat)):
        summ = 0
        res.append(sum(mat[i]))
    return res
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print('#'*18,' '*18)
print('')

def col_sums(mat: list[list[float | int]]) -> list[float]:
    rvan = [len(x) for x in mat]
    if len(set(rvan)) != 1:
        raise ValueError
    res = []
    for i in range(len(mat[0])):
        s = 0
        for j in range(len(mat)):
            s+=mat[j][i]
        res.append(s)       
    return res
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
print('#'*18)
```
![matrix](./images/lab02/ex02.png)
## Задание 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
        raise TypeError #Проверка на кортеж
    if len(rec) != 3:
        raise ValueError #Отсутствуют элементы 
    fio, group,gpa = rec
    if  group == '' or gpa > 5 or gpa < 0 or fio == '':
        raise ValueError #Неверные данные(0<gpa<5)
    if not isinstance(gpa,(int,float)) or not isinstance(group,str) or not isinstance(fio,str):
        raise TypeError #Неверный тип данных  
    stroka = ''
    inic = fio.strip().split()
    if len(inic) == 3:
        inic = str(inic[0][0].upper()+inic[0][1::] + ' ' +(inic[1])[:1:].upper()+'.'+ (inic[2])[:1:].upper()+'.')
    else:
        inic = str(inic[0][0].upper()+inic[0][1::]  +' '+(inic[1])[:1:]+'.')    
    grupa = rec[1]
    ball = f'{gpa:.2f}'
    stroka = inic + ', гр. ' + grupa + ', GPA ' + ball 
    return stroka
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", 5,4.0)))  
print('#'*18)
```
![tuples](./images/lab02/ex03.png)

# Лабораторная работа 2
## Задание 1 (Функции)
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if text == '': return ''
    if casefold: 
        text = text.casefold()
    if yo2e:
        text = text.replace('ё','е').replace('Ё','Е')
    text = ' '.join(text.split())
    return text
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
print('#'*18)
print(' '*18)

def tokenize(text: str) -> list[str]:
    tokenn = []
    perederz = []
    for simv in text+' ':
        if simv.isalnum() or simv == '_':
            perederz.append(simv)
        elif simv == '-' and len(perederz)>=1 and perederz[-1].isalnum():
            perederz.append(simv)        
        else:
            if len(perederz) >=1:   
                tokenn.append(''.join(perederz))
                perederz = []
    return tokenn 
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
print('#'*18)
print(' '*18)

def count_freq(tokens: list[str]) -> dict[str, int]:
    slovar = {}
    for token in tokens:
        slovar[token] = slovar.get(token,0) +1
    return slovar
print(count_freq(["a","b","a","c","b","a"]))
print('#'*18)
print(' '*18) 

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    res = list(freq.items())
    res.sort(key = lambda i: (-i[1],i[0]))
    return res
print(top_n({"bb":2,"aa":2,"cc":3}))
print('#'*18)
print(' '*18)
```
![func](./images/lab03/text.png)

## Задание 2 
```python 
import sys
import os
from pathlib import Path

lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from text import tokenize, normalize, count_freq, top_n


def read_stdin() -> str:
    return sys.stdin.read()


def stats(colvo_slov: int, unik_slova: int, top_items):
    print(f'Всего слов: {colvo_slov}')
    print(f'Уникальных слов: {unik_slova}')
    print('Топ-5:')
    for word, count in top_items:
        print(f'{word}:{count}')


def main():
    text = read_stdin()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq_map = count_freq(tokens)
    top = top_n(freq_map, 5)
    stats(len(tokens), len(set(tokens)), top)


if __name__ == '__main__':
    main()
```
![text_stats](./images/lab03/text_stats.png)