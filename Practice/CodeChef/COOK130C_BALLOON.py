t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    save = set()
    for val in a:
        if len(save) == 7:
            break
        if val <= 7:
            save.add(val)
        count += 1
    print(count)