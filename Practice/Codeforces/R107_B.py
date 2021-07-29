t = int(input())
for i in range(t):
    a, b, c = tuple(map(int, input().split()))
    x = 10**(a-1)
    y = 10**(b-1)
    gcd = 10**(c-1)
    print(x, y + gcd)

# def gcd(a, b) :
#     if (a == 0) :
#         return b
#     return gcd(b % a, a)

# def isPrime(n):
#     if (n <= 1):
#         return False
#     for i in range(2, n):
#         if (n % i == 0):
#             return False
#     return True

# def find_num_gcd(lst):
#     a = lst[0]
#     b = lst[1]
#     c = lst[2]
#     for i in range(10**(c-1),10**c):
#         if isPrime(i):
#             t1 = i
#             break
#     if (a - c > 0):
#         for i in range(10**(a-c-1), 10**(a-c)):
#             if isPrime(i):
#                 t2 = i
#                 break
#     else:
#         for i in range(10**(a-1), 10**(a)):
#             if isPrime(i):
#                 t2 = i
#                 break
#     if (b-c > 0):
#         for i in range(10**(b-c-1), 10**(b-c)):
#             if isPrime(i):
#                 t3 = i
#                 break
#     else:
#         for i in range(10**(b-1), 10**(b)):
#             if isPrime(i):
#                 t3 = i
#                 break
#     return t1*t2, t1*t3

# for i in range(t):
#     res = find_num_gcd(lst[i])
#     print(res[0], res[1])



 
