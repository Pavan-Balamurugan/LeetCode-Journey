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

# Time Complexity: O(n)
# Space Complexity: O(n)    


# The above code defines a function `twoSum` that takes a list of integers `nums` and
# an integer `target`. It uses a hash map (dictionary) to store previously seen numbers 
# and their indices. For each number in the list, it calculates the complement 
# (the number needed to reach the target) and checks if it exists in the hash map.
# If it does, it returns the indices of the two numbers. If not, it adds the current number
# and its index to the hash map.