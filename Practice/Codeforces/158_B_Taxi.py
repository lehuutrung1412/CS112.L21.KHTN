import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)
count = 0
i = 0
while (i < n):
    if s[i] == 4:
        count += 1
        i += 1
    else:
        sum = s[i]
        while (i < n and sum + s[n-1] <= 4):
            sum += s[n-1]
            n -= 1
        count += 1
        i += 1
print(count)    