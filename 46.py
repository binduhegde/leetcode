# def factorial(n):
#     if n == 1: return 1
#     return n * factorial(n-1)

# def permutation_recursion(lst):
#     if len(lst) == 2:
#         return [lst, lst[::-1]]
#     for element in range(len(lst)):
#         if element == 0: result = []
#         lstcopy = lst[:]
#         constant = lstcopy[element]
#         lstcopy.remove(lstcopy[element])
#         recursion_result = permutation_recursion(lstcopy)
#         for i in range(factorial(len(lstcopy))):
#             result += [list(constant) + [i for i in recursion_result[i]]]
#     return result


# def factorial(n):
#     if n < 2: return n
#     return factorial(n-1) * n

# def permutations(nums):
#     nums = [str(i) for i in nums]
#     if len(nums) == 1: return [nums]
#     elif len(nums) == 2:
#         return [nums, nums[::-1]]
#     result = []
#     for i in range(len(nums)):
#         nums_copy = nums.copy()
#         constant = nums_copy[i]
#         nums_copy.remove(nums_copy[i])
#         recursion_result = permutations(nums_copy)
#         for i in range(factorial(len(nums_copy))):
#             result += [[int(constant)]+ [int(j) for j in recursion_result[i]]]
#     return result

# print(permutations([1,2,3,4]))

def permutations(nums):
    result = []

    # if there is only one element in the nums, i.e., if we have reached 
    # the end of recursion, it only return that number in a list of list
    if len(nums) == 0:
        return [nums[:]]
    
    for i in range(len(nums)):
        # pops the first element and saves it under 'n'
        n = nums.pop(0)
        # keeps recursing until there's only one item in the list
        perms = permutations(nums)

        for perm in perms:
            # adds the popped value at the end of each permutation
            perm.append(n)
        # adds all the permutations with ith value at the last
        result.extend(perms)
        # adds back the value we popped earlier
        nums.append(n)

    return result

#print(permutations([1,2,3,4]))

# this is in the right order 
def permutations2(nums):
    result = []

    if len(nums) == 2:
        return [nums[:], nums[::-1]]
    
    for i in range(len(nums)):
        n = nums.pop(i)
        perms = permutations2(nums)

        for perm in perms:
            perm.insert(0, n)
        result.extend(perms)
        nums.insert(i, n)

    return result
    