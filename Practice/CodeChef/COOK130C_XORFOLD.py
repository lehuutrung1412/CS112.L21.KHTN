t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for _ in range(n):
        cnt += input().count('1')
    if cnt & 1:
        print('YES')
    else:
        print('NO')