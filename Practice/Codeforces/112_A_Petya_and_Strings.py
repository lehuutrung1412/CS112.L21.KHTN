a = input()
b = input()
a = a.lower()
b = b.lower()
if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)