def product_except_self(arr):
    n = len(arr)
    result = [1] * n
    
    # Pass 1: result[i] = product of everything LEFT of i
    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]
    
    # Pass 2: multiply result[i] by product of everything RIGHT of i
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= arr[i]
    
    return result

arr = [1, 2, 3, 4]
print("Original array:", arr)
print("Product array except self:", product_except_self(arr))