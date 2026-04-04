def twoSum(nums, target):
    prevMap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in prevMap:
            return [prevMap[complement], i]
        prevMap[num] = i

a = list(map(int, input().split()))
target = int(input())
print(twoSum(a, target))