t = int(input())
r = []
for i in range(t):
    n = int(input())
    temp = list(map(int, input().split()))
    r.append(temp)

def find_upvote(lst):
    up = 0
    for i in range(len(lst)):
        if (lst[i] == 1 or lst[i] == 3): up += 1
    return up

for i in range(t):
    print(find_upvote(r[i]))