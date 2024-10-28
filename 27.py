def remove_element(nums, val):
    nums = [i for i in nums if i != val]
    return len(nums), nums

print(remove_element([3,2,2,3], 3))
print(remove_element([0,1,2,2,3,0,4,2], 2))

