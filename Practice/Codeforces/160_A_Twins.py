n = int(input())
coins = list(map(int, input().split()))
coins = sorted(coins, reverse=True)
sum_coin = sum(coins)
num = 0
count = 0 
while (num <= sum_coin - num):
    num += coins[count]
    count += 1
print(count)