s = input()
n = len(s)
flag = False
for i in range(1, n):
    if s[i].islower():
        flag = True
if flag == False:
    print(s.swapcase())
else:
    print(s)
    