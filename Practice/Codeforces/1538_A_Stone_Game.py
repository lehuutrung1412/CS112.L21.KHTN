import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def count_move(a):
    min_idx = max_idx = 0
    min_val = max_val = a[0]
    half = (n-1)//2
    for i in range(1, n):
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
        if a[i] <= min_val:
            min_val = a[i]
            min_idx = i
    if min_idx <= half:
        step_min = min_idx
    else:
        step_min = n-1-min_idx
    if max_idx <= half:
        step_max = max_idx
    else:
        step_max = n-1-max_idx
    return min(max(min_idx, max_idx)+1, step_max+step_min+2, max(n-1-min_idx, n-1-max_idx)+1)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count_move(a))