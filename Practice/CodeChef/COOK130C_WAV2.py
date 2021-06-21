import bisect

def mul():
    small = bisect.bisect(a, x)
    if x != a[small-1]:
        if (n - small) & 1:
            print('NEGATIVE')
            return
        else:
            print('POSITIVE')
            return
    else:
        print('0')
        return
    
n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for _ in range(q):
    x = int(input())
    mul()
        