# lol

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
kolich_ychast = int(input('in_1: '))
ochno = 0
zaochno = 0
for i in range(kolich_ychast):
    ychastnik = input(f'in_{i+2}: ')
    if 'True' in ychastnik:
        ochno +=1
    else:
        zaochno+=1
print(f'out: {ochno} {zaochno}')
```
![zvezdochka#6](./images/lab01/ex06.png)

## Задание 7
```python
vxod = input('in: ')
slovo = ''
index1 = 0 
index2 = 0

for i in range(len(vxod)):
    if vxod[i].isupper():
        index1 = i 
        break
    else:
        continue 
for i in range(len(vxod)):
    if vxod[i] in '0123456789':
        index2 = i+1
        break
    else:
        continue
shag = index2 - index1
for i in range(index1,len(vxod),shag):
    slovo+=vxod[i]
print(f'out: {slovo}')
```
![zvezdochka#7](./images/lab01/ex07.png)

