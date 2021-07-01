n = int(input())
sum  = 0
for i in range(n):
    a, b, c = map(int, input().split())
    all = 4*a + 2*b + c
    if (all == 3 or all == 5 or all == 6 or all == 7):
        sum += 1
print(sum)