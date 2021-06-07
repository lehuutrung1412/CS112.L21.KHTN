import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m = map(int, input().split())
adj = dict()
count = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    if u < 1 or u > n or v < 1 or v > n:
        continue
    u -= 1
    v -= 1
    if u not in adj:
        adj[u] = {v}
    else:
        adj[u].add(v)
    count[v] += 1

def get_result():
    if count.count(0) > 1:
        print('No')
        exit()
    root = count.index(0)
    parent = [-1] * n
    visited = [False] * n
    queue = [root]
    while queue:
        this_node = queue.pop()
        visited[this_node] = True
        for child in adj[this_node]:
            if parent[child] == -1:
                parent[child] = this_node
            else:
                if this_node not in adj[parent[child]]:
                    print('No')
                    exit()
                else:
                    parent[child] = this_node
            if not visited[child]:
                try:
                    adj[child]
                    queue.append(child)
                except KeyError:
                    continue
    print('Yes')
    for element in parent:
        if element != -1:
            print(element + 1, end=' ')
        else:
            print(-1, end=' ')
        
get_result()


# import io, os
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# n, m = map(int, input().split())
# adj = dict()
# for i in range(m):
#     u, v = map(int, input().split())
#     if u < 1 or u > n or v < 1 or v > n:
#         continue
#     u -= 1
#     v -= 1
#     if u not in adj:
#         adj[u] = {v}
#     else:
#         adj[u].add(v)

# def traversal(node, visited, parent):
#     visited[node] = True
#     flag = False
#     try:
#         for child in adj[node]:
#             if not visited[child]:
#                 flag = True
#                 child_node = traversal(child, visited, parent)
#                 parent[child_node] = node
#         if flag == False:
#             print('No')
#             exit()
#         return node   
#     except KeyError:
#         return node 

# def main():
#     visited = [False] * n
#     parent = [-2] * n
#     for node in adj:
#         if not visited[node]:
#             traversal(node, visited, parent)
#     print('Yes')
#     for value in parent:
#         print(value + 1, end=' ')
        
# main()

                    
# while queue:
#     this_node = next(iter(queue))
#     queue.discard(this_node)
#     visited[this_node] = True
#     for child in adj[this_node]:
#         if parent[child] == -1:
#             parent[child] = this_node
#         else:
#             if this_node not in adj[parent[child]]:
#                 if parent[child] not in adj[this_node]:
#                     print('No')
#                     exit()
#             else:
#                 parent[child] = this_node
#         if not visited[child]:
#             try:
#                 adj[child]
#                 queue.add(child)
#             except KeyError:
#                 continue
# print('Yes')
# for element in parent:
#     if element != -1:
#         print(element + 1, end=' ')
#     else:
#         print(-1, end=' ')     