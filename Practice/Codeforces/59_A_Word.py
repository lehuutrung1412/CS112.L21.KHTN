s = input()
lower = 0
for char in s:
    if char >= 'a' and char <= 'z':
        lower += 1
if lower >= len(s) - lower:
    print(s.lower())
else:
    print(s.upper())