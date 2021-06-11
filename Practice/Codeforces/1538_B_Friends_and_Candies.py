import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def choose_k(a):
    sum_ = sum(a)
    if sum_ % n != 0:
        return -1
    else:
        avg = sum_ // n
        count = 0
        for val in a:
            if val > avg: count += 1
        return count

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(choose_k(a))