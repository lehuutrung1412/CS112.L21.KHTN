n, k = map(int, input().split())
while (k != 0):
    mod = n % 10
    if mod == 0:
        n = n // 10
        k -= 1
    else:
        remain = k - mod
        if remain <= 0:
            n -= k
            k -= k
        else:
            n -= mod
            k -= mod
print(n)