t = int(input()) 
for i in range(t):
    n = int(input())
    s = input()
    lst = []
    flag = 1
    for i in s:
        if i not in lst:
            lst.append(i)
        elif i == lst[-1]:
            continue
        else:
            flag = 0
            break
    if flag == 1:
        print('YES')
    else:
        print('NO')