guest = input()
host = input()
string = input()
if sorted(guest + host) == sorted(string):
    print('YES')
else:
    print('NO')