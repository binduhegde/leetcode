def kth_factorial(n,k):
    nums = [str(i) for i in range(1, n+1)]
    factorial = [1] * (n+1)
    for i in range(1, n+1):
        factorial[i] = factorial[i-1] * i
    k -= 1  # Adjust k to match 0-indexing
    
    result = []
    for i in range(n, 0, -1):
        index = k // factorial[i-1]
        k %= factorial[i-1]
        result.append(nums.pop(index))
    
    return ''.join(result)

print(kth_factorial(3,4))
#print(kth_factorial(1,1))
