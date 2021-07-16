n, k = map(int,input().split())
a = list(map(int, input().split()))

def choose(a):
    if a[k-1] == 0:
        for i in range(k-2,-1,-1):
            if a[i] > 0:
                return i+1
        return 0
    for i in range(k, n):
        if a[i] < a[k-1]:
            return i
    return n

print(choose(a))
