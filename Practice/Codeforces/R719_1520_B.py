t = int(input())

def find_total_ordinary(n):
    num = len(n)
    res = (num - 1) * 9
    n = int(n)
    mod = int('1' * num)
    res += n // mod
    return res

for i in range(t):
    n = input()
    print(find_total_ordinary(n))