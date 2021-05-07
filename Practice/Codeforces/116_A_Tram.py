n = int(input())
max_ = 0
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += b - a
    max_ = max(max_, sum)
print(max_)