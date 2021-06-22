n, m, a = map(int, input().split())
if (n % a == 0):
    len = n//a
else:
    len = n//a + 1
if (m % a == 0):
    bre = m//a
else:
    bre = m//a + 1
print(len * bre)