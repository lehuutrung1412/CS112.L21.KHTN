s = input()
num = []
for i in s:
    if i != '+':
        num.append(i)
num = sorted(num)
res = str(num[0])
for i in range(1, len(num)):
    res += '+' + str(num[i])
print(res)