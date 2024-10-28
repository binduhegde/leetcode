import numpy

def product_except_self(nums):
    zeroes = []
    product = 1
    
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes.append(i)
            if len(zeroes) > 1: return [0 for i in nums]
        else: product *= nums[i]
    
    if len(zeroes) == 1:
        result = [0 for i in nums]
        result[zeroes[0]] = product
    else:
        result = [product//i for i in nums]
    return result


print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))