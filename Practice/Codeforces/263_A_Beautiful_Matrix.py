for i in range(5):
    temp = list(map(int, input().split()))
    if 1 in temp:
        pos = [i, temp.index(1)]
print(abs(pos[0] - 2) + abs(pos[1] - 2))
