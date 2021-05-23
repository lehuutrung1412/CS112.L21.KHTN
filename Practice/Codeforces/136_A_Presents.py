import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
received = list(map(int, input().split()))
gave = [(i, j) for i, j in enumerate(received, 1)]
gave.sort(key=lambda tup: tup[1])
for element in gave:
    print(element[0], end=" ")