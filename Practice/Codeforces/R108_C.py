t = int(input())
for j in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))
    uni = dict()
    for i in range(n):
        if u[i] not in uni:
            uni[u[i]] = [s[i]]
        else:
            uni[u[i]].append(s[i])
    res = {z:0 for z in range(1, n+1)}
    for key in uni:
        uni[key].sort(reverse=True)
        for x in range(1, len(uni[key])):
            uni[key][x] += uni[key][x-1]
        for k in range(1, n+1):
            index = len(uni[key])//k*k - 1
            if index == -1:
                break
            res[k] += uni[key][index]
    print(*res.values())