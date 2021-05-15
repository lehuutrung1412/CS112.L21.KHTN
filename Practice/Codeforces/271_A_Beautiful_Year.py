year = input()
while 1:
    year = str(int(year) + 1)
    if year[0] != year[1] and year[0] != year[2] and year[0] != year[3] and year[1] != year[2] and year[1] != year[3] and year[2] != year[3]:
        break
print(year)