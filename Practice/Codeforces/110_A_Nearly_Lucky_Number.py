n = input()

def is_lucky_num(num):
    if num < 4:
        return False
    constraint = [4, 7]
    while(num != 0):
        mod = num % 10
        if mod not in constraint:
            return False
        num //= 10
    return True

num = 0
for i in n:
    if i == '4' or i == '7':
        num += 1
if is_lucky_num(num):
    print("YES")
else:
    print("NO")