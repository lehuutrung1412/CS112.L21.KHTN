n = int(input())
c = list(map(int, input().split()))

def hIndex(n,c):
    c.sort(reverse=True)
    for i in range(n,0,-1):
        if (i <= c[i-1]):
            return i
    return 0

print(hIndex(n,c))