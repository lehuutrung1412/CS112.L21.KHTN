s = input()
res = s.replace('WUBWUB', ' ')
res = res.replace('WUB', ' ')
i = 0
while (res[i] == ' '):
    res = res[i+1:]
print(res)