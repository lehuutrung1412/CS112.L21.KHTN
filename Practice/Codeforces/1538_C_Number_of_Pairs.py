import io, os
import bisect
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def count_num_pair():
    count = 0
    for i in range(n):
        min_ = bisect.bisect_left(a, l - a[i])
        min_ = max(min_, i+1)
        max_ = bisect.bisect_right(a, r - a[i])
        if max_ >= min_:
            count += max_ - min_
    return count
        

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(count_num_pair())