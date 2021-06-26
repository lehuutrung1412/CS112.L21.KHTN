s = input()
for i in range(len(s)-6):
    s_cut = s[i:i+7]
    if s_cut == '0000000' or s_cut == '1111111':
        print('YES')
        exit()
print('NO')