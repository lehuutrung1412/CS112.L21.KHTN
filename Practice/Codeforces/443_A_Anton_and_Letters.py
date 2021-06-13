s = input()
print(len(set(s[1:-1].split(", ")))) if len(s) > 2 else print(0)