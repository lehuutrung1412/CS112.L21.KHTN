t = int(input())

for i in range(t):
    n = int(input())
    a = input()
    count_T = 0
    for i in a:
        if i == 'T':
            count_T += 1
        else:
            count_T -= 1
        if count_T < 0 or count_T > n//3:
            break
    if (count_T == n // 3):
        print('YES')
    else:
        print('NO')
    

