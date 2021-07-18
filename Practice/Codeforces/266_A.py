n = int(input())
s = input()
count = 0
for i in range(n-1):
    if (s[i] == s[i + 1]):
        count += 1
print(count)
