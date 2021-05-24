# import io, os
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def fix_fence(fence, wood):
    choose_fence = min(fence)
    choose_wood = max(wood)
    left = choose_fence
    right = choose_fence + choose_wood + 1
    while (left < right):
        new_height = (left + right) >> 1
        j = 0
        flag = True
        for height in fence:
            if height < new_height:
                flag = False
                while (j < m):
                    if (height + wood[j] < new_height):
                        j += 1
                    else:
                        j += 1
                        flag = True
                        break
                if flag == False:
                    break
        if flag == True:
            left = new_height + 1
        else:
            right = new_height
    return left-1, choose_fence

def get_result(fence, wood, new_height, min_fence):
    res = []
    j = 0
    for i, height in enumerate(fence, 1):
        if height < new_height or height == min_fence:
            while (j < m):
                if (height + wood[j] < new_height):
                    j += 1
                else:
                    j += 1
                    res.append((i, j))
                    break
    return res

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

height, min_fence = fix_fence(a, b)
res = get_result(a, b, height, min_fence)
print(height, len(res))
for i in res:
    print(*i)                