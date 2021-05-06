t = int(input())
for i in range(t):
    a, b, c = tuple(map(int, input().split()))
    x = 10**(a-1)
    y = 10**(b-1)
    gcd = 10**(c-1)
    print(x, y + gcd)
