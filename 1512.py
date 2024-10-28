def factorial(n):
    f = n
    for i in range(2, n):
        f *= i
    return f

def numIdenticalPairs(nums):
    count = 0
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) +1
    
    for key, value in d.items():
        if value == 1: continue
        elif value == 2: count+=1
        else:
            count += factorial(value)//(factorial(2)*factorial(value-2))
    return count

print(numIdenticalPairs([1,1,1,1]))

