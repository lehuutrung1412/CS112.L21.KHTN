import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def is_palind(x):
    return str(x) == str(x)[::-1]

def cal_sum_palind(n, d):
    res = set()
    i = 1
    while (2*i*i < n):
        next = i + d
        temp = i*i + next * next
        while (temp < n):
            if is_palind(temp):
                res.add(temp)
            next += d
            temp += next * next
        i += 1
    return sum(res)    
                 
num_testcase = int(input())
for _ in range(num_testcase):
    n, d = map(int, input().split())
    print(cal_sum_palind(n, d))
    