vxod = input('in: ')
itog = ''
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
    itog+=vxod[i]
print(f'out: {itog}')
