def matMul(a,b):
    c = [[0,0],[0,0]]
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return c

def matrixFibonacci(n):
  a = [[1,1],[1,0]]
  if (n == 1):
    return a
  if (n % 2 == 0):
    return matMul(matrixFibonacci(n // 2), matrixFibonacci(n // 2))
  else:
    return matMul(matMul(matrixFibonacci(n // 2), matrixFibonacci(n // 2)),a)

def fibonacci(n):
  return matrixFibonacci(n)[0][0]

n,k = map(int,input().split())
print(fibonacci(2*k)*n % 1000000007)

""" Old method
n,k = map(int, input().split())
x = 1
y = 0
for i in range(1, k+1):
    x_curr = x + y
    y_curr = x + 2*y
    x = x_curr
    y = y_curr
sum = (x + y) * n % 1000000007
print(sum)
"""