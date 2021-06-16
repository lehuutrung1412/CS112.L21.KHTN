n = int(input())
s = input()
s = s.lower()
for c in range(97, 123):
    if chr(c) not in s:
        print("NO")
        exit()
print("YES") 