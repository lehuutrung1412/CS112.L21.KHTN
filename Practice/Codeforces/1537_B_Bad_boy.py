t = int(input())
for _ in range(t):
    n, m, i, j = map(int, input().split())
    if (i <= n / 2 and j <= m / 2) or (i >= n / 2 and j >= m / 2):
        print(1,m,n,1)
    else:
        print(1,1,n,m)