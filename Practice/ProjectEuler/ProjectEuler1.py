t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    k_of_3 = (n-1) // 3
    k_of_5 = (n-1) // 5
    k_of_15 = (n-1) // 15
    sum_ = k_of_3*(k_of_3+1)*3//2 + k_of_5*(k_of_5+1)*5//2 - k_of_15*(k_of_15+1)*15//2
    print(sum_)
