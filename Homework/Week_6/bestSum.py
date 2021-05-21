def findBestSum(arr, sum, memo = {}):
    if sum in memo:
        return memo[sum]
    elif sum < 0:
        return None
    elif sum == 0:
        return []
    min_element = None
    for num in arr:
        remain = sum - num
        sum_remain = findBestSum(arr, remain)
        if not sum_remain is None:
            element = [num]
            element += sum_remain
            if min_element is None or len(min_element) > len(element):
                min_element = element
    memo[sum] = min_element
    return min_element
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(*findBestSum(arr, k))