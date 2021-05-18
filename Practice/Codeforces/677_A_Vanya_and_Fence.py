n, h = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for height_person in a:
    if height_person <= h:
        count += 1
    else:
        count += 2
print(count)