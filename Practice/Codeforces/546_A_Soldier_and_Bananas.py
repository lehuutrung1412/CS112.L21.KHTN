k, n, w = map(int, input().split())
res = w*(w+1)//2 * k - n
if res <= 0:
    print(0)
else:
    print(res)