def k_diff(nums, k):
    c = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if abs(nums[i]-nums[j]) == k: c +=1
    return c 

print(k_diff([1,2,2,1], 1))