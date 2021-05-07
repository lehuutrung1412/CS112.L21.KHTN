t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if b == 1:
        print("NO")
        continue
    print("YES")
    print(a, end=" ")
    if b > 2:
        print(a * (b - 1), end=" ")
        print(a * b)
    else:
        print(a * (3*b - 1), end=" ")
        print(3*a*b)