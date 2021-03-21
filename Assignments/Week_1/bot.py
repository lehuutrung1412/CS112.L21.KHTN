from sys import maxsize

n = int(input())
a = list(map(int,input().split()))[:n]

def findMaxSub(a, n):
    best = -maxsize - 1
    start = end = startTemp = sum = 0
    for i in range(0,n):
        if (a[i] < sum + a[i]):
            sum += a[i]
        else:
            startTemp = i
            sum = a[i]
        if (sum > best):
            best = sum
            start = startTemp
            end = i
    return start + 1, end + 1, best

start, end, maxSub = findMaxSub(a,n)
print(start, end, maxSub)