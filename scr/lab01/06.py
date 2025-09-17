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
