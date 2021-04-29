a, k, b, m, n = map(int,input().split())
date = 0
while n >= (a + b):
    yesterday = date
    date += n//(a+b)
    n = n % (a + b) + a * (date//k - yesterday//k) + b * (date//m - yesterday//m)
while n > 0:
    date += 1
    n -= int(date % k != 0) * a + int(date % m != 0) * b
print(date)