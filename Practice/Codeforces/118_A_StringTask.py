str = input()
str = str.lower()
vowel = 'aoyeui'
for i in vowel:
    str = str.replace(i, '')
res = ''
for i in str:
    res += '.'
    res += i
print(res)
