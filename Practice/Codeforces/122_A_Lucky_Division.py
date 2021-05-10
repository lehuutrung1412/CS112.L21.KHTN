def is_lucky_num(num):
    constraint = [4, 7]
    while(num != 0):
        mod = num % 10
        if mod not in constraint:
            return False
        num //= 10
    return True

n = int(input())
for i in range(4, n+1):
    if is_lucky_num(i) and n % i == 0:
        print("YES")
        exit()
print("NO")