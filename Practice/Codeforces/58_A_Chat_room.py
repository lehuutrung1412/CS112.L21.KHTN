s = input()
right_string = "hello"
j = 0
for i in s:
    if i == right_string[j]:
        j += 1
    if j == 5:
        print("YES")
        exit()
print("NO")