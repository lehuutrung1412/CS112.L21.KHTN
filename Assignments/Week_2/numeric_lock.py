a = input().strip()
listInt = [int(i) for i in a]
listInt.sort(reverse=True)

sumList = sum(listInt)
dem = [0 for _ in range(3)]
listMod1 = []
listMod2 = []
for i in listInt:
    dem[i % 3] += 1
    if (i % 3 == 1): listMod1.append(i) 
    if (i % 3 == 2): listMod2.append(i) 

if sumList % 3 == 1:
    if dem[1] > 0:
        listInt.remove(listMod1[-1])
    else:
        for i in listMod2[-2:]:
            listInt.remove(i)
elif sumList % 3 == 2:
    if dem[2] > 0:
        listInt.remove(listMod2[-1])
    else:
        for i in listMod1[-2:]:
            listInt.remove(i)

print(''.join([str(i) for i in listInt]))