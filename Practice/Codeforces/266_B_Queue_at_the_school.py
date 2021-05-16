n, t = map(int, input().split())
s = input()
while (t != 0):
    change = 0
    i = 0
    while (i < n-1):
        if s[i] == 'B' and s[i+1] == 'G':
            s = s[:i] + 'G' + 'B' + s[i+2:]
            change = 1
            i += 1
        i += 1
    if change == 0:
        break
    t -= 1
print(s)