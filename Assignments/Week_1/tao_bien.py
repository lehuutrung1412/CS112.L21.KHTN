n,k = map(int, input().split())
x = 1
y = 0
for i in range(1, k+1):
    x_curr = x + y
    y_curr = x + 2*y
    x = x_curr
    y = y_curr
sum = (x + y) * n % 1000000007
print(sum)