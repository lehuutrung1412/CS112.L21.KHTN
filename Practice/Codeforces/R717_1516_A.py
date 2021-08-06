t = int(input())

def small_lexi(a, n, k):
    for i in range(n):
        if a[i] > 0:
            break
    for j in range(n-1, -1, -1):
        if a[j] > 0:
            break
    if i == j:
        return sorted(a)
    while (i < j and k != 0 and a[i] > 0 and a[j] > 0):
        if a[i] > 1:
            a[i] -= 1
            a[j] += 1
            k -= 1
        else:
            i += 1
    return a
        
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(*small_lexi(a, n, k))
