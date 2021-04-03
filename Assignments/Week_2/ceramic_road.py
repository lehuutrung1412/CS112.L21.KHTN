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
    team1 = []
    team2 = []
    for i in range(0, numPart):
        if sorted(a[0:lenPart]) == sorted(a[lenPart*i:lenPart*(i+1)]):
            if not team1: team1 = a[0:lenPart]
            demP += 1
        else:
            if team2 and sorted(a[lenPart*i:lenPart*(i+1)]) != sorted(team2):
                demQ = 0
                break
            elif not team2:
                team2 = a[lenPart*i:lenPart*(i+1)]
            demQ += 1
    if demP < demQ:
        demP, demQ = demQ, demP
    if demQ != 0:
        result.append([lenPart,demP,demQ])

numSolution = len(result)
if numSolution == 0:
    print(-1)
else:
    print(numSolution)
    for solution in result:
        print(*solution)


# for i in range(1, numPart):
    #     if set(a[0:lenPart]) != set(a[lenPart*i:lenPart*(i+1)]):
    #         team1 = a[0:lenPart]
    #         team2 = a[lenPart*i:lenPart*(i+1)]
    # for i in range(0, numPart):
    #     if set(a[lenPart*i:lenPart*(i+1)]) == set(team1):
    #         demP += 1
    #     elif set(a[lenPart*i:lenPart*(i+1)]) == set(team2):
    #         demQ += 1
    #     else:
    #         demQ = 0
    #         break

# if (j+1)*i+i <= n:
#     if set(a[0:i]) != set(a[(j+1)*i:(j+1)*i+i]) != set(a[j*i:j*i+i]):
#         demQ = 0
#         break


# if set(a[0:lenPart]) == set(a[lenPart*i:lenPart*(i+1)]):
            
#             demP += 1
#         else:
#             if lenPart*(i+2) <= n:
#                 if set(a[0:lenPart]) != set(a[lenPart*(i+1):lenPart*(i+2)]) != set(a[lenPart*i:lenPart*(i+1)]):
#                     demQ = 0
#                     break
#             demQ += 1