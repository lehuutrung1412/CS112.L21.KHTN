n, m = map(int, input().split())
a = list(map(int, input().split()))
count = a[0] - 1
for i in range(1, m):
    if a[i] >= a[i-1] and a[i] <= n:
        count += a[i] - a[i-1]
    elif a[i] < a[i-1]:
        count += n - a[i-1] + a[i]
print(count)
    