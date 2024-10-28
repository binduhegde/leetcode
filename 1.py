def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i

print(two_sum([2,15,7,11], 9))
print(two_sum([3,3], 6))
