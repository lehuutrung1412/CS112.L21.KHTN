t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    if m * n - 1 == k:
        print('YES')
    else:
        print('NO')