t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1:
        print('Bob')
    else:
        count = 0
        while(n % 2 == 0):
            n //= 2
            count += 1
        if n > 1:
            print('Alice')
        else:
            if count % 2:
                print('Bob')
            else:
                print('Alice')