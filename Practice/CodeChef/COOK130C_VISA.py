t = int(input())
for _ in range(t):
    x1, x2, y1, y2, z1, z2 = map(int, input().split())
    if x2 < x1 or y2 < y1 or z2 > z1:
        print('NO')
    else:
        print('YES')