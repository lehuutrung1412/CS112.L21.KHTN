nVer, nEdge = map(int, input().split())
adj = {}
for i in range(nEdge):
    u, v, w = map(int, input().split())
    try:
        adj[u].append((w, v))
    except:
        adj[u] = [(w, v)]
    try:
        adj[v].append((w, u))
    except:
        adj[v] = [(w, u)]
a, b, k = map(int, input().split())
        

def count_paths():
    queue = [(0, a, -1)]
    visited = []
    count = 0
    while queue:
        total, ver, prev = queue.pop(0)
        if total == k and ver == b:
            count += 1
            continue
        elif total > k or (ver == b and total != k):
            continue
        else:
            for weight, nextVer in adj[ver]:
                if (prev, ver, nextVer) not in visited:
                    visited.append((prev, ver, nextVer))
                    queue.append((total + weight, nextVer, ver))
    return count if count > 0 else -1

print(count_paths())

''' Testcase
4 5
0 1 1
0 2 1
1 3 1
2 3 1
2 1 3
0 3 5

5 7
0 1 3
0 3 5
1 3 2
2 0 1
3 4 1
4 1 1
2 3 2
0 3 5

6 10                                                              
0 1 5
0 5 8
1 4 6
1 3 2
2 5 11
2 3 1
3 0 4
3 4 3
4 5 2
5 3 5
3 5 12
'''