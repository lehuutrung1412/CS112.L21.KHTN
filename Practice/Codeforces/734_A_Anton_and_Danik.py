n = int(input())
res = input()
anton = 0
for i in res:
    if i == 'A':
        anton += 1
if anton > n - anton:
    print("Anton")
elif anton < n - anton:
    print("Danik")
else:
    print("Friendship")