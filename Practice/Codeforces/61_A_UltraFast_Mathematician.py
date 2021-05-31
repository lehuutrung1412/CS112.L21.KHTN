part_1 = input()
part_2 = input()
n = len(part_1)
res = ''
for i in range(n):
    res += str(int(part_1[i])^int(part_2[i]))
print(res)