def doiso_bf(x):
    res = 0
    for i in range(len(x)):
        for j in range(10):
            if j != int(x[i]):
                tmp = x[:i] + str(j) + x[i+1:]
            if int(tmp) % 3 == 0:
                res = max(res, int(tmp))
    if res == x:
        res -= 3
    return res

a = input().strip()
res = doiso_bf(a)
print(res)