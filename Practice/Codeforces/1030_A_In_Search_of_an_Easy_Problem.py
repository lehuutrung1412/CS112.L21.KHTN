n = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if i == 1:
        print('HARD')
        exit()
print('EASY')