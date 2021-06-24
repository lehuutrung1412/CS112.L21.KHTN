n = int(input())
sum = [0, 0, 0]
for i in range(n):
    x, y, z = map(int, input().split())
    sum[0] += x
    sum[1] += y
    sum[2] += z
if sum == [0, 0, 0]:
    print('YES')
else:
    print('NO')