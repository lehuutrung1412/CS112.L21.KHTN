def is_palindrome(str):
  return str == str[::-1]

def longest_palind(str):
    n = len(str)
    result = ''
    for i in range(n):
        for j in range(i, n):
            if str[i] == str[j]:
              s = str[i:j+1]
              if (is_palindrome(s) and len(s) > len(result)):
                  result = s
    return len(result), result

try:
    str = input()
except EOFError:
    str = ''
print(*longest_palind(str))