import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m = map(int, input().split())
adj = dict()
for i in range(m):
    u, v = map(int, input().split())
    if u < 1 or u > n or v < 1 or v > n:
        continue
    if u not in adj:
        adj[u] = [v]
    else:
        adj[u].append(v)
    if v not in adj:
        adj[v] = [u]
    else:
        adj[v].append(u)

def findConnectedCom():
    visited = [False] * (n+1)
    connectedComs = 1
    queue = []
    count = 0
    for i in adj:
        if not visited[i]:
            count += 1
            begin_count = visited.count(True)
            queue.append(i)
            while queue:
                select = queue.pop(0)
                for j in adj[select]:
                    if not visited[j]:
                        queue.append(j)
                        visited[j] = True
            end_count = visited.count(True)
            count_ver = end_count - begin_count
            if count_ver > 1:
                connectedComs = connectedComs * count_ver
    return n - visited.count(True) + count, connectedComs

numCons, res = findConnectedCom()
MOD = 1000000007
print(numCons - 1)
if numCons == 1:
    print(0)
else:
    num_way = pow(n, numCons - 2, MOD)
    res = (res * num_way) % MOD
    print(res)