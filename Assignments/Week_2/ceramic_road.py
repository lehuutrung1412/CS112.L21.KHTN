import math

n = int(input())
a = list(map(int, input().split()))

numParts = [n]
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        numParts.append(i)
        numParts.append(int(n/i))
numParts = list(set(numParts))
numParts.sort(reverse=True)
result = []
for numPart in numParts:
    demP = 0
    demQ = 0
    lenPart = int(n/numPart)
    team2 = []
    for i in range(0, numPart):
        if sorted(a[0:lenPart]) == sorted(a[lenPart*i:lenPart*(i+1)]):
            demP += 1
        else:
            if (team2 and sorted(a[lenPart*i:lenPart*(i+1)]) != sorted(team2)):
                demQ = 0
                break
            elif not team2:
                team2 = a[lenPart*i:lenPart*(i+1)]
            demQ += 1
    # This is a bug for testcase 4
    # if demP < demQ:
    #     demP, demQ = demQ, demP
    if demQ != 0:
        result.append([lenPart,demP,demQ])

numSolution = len(result)
if numSolution == 0:
    print(-1)
else:
    print(numSolution)
    for solution in result:
        print(*solution)