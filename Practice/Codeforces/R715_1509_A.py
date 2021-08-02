t = int(input())

def sort_avg(lst, n):
    even = []
    odd = []
    for i in range(n):
        if (lst[i] & 1):
            odd.append(lst[i])
        else:
            even.append(lst[i])
    return odd + even
    
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(*(sort_avg(a, n)))
    

