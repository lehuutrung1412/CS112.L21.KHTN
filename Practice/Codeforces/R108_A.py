t = int(input())
for i in range(t):
    r, b, d = map(int, input().split())
    if r < b:
        r, b = b, r
    if (r - b) / b > d:
        print('NO')
    else:
        print('YES')