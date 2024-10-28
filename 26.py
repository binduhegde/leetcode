def remove_dup(nums):
    # removed = []
    # for i in nums:
    #     if i not in removed: removed.append(i)

    # for i in range(len(nums)):
    #     try:
    #         nums[i] = removed[i]
    #     except: nums[i] = 0
    # return len(removed)
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j,  nums


#print(remove_dup([0,0,1,1,1,2,2,3,3,4]))
print(remove_dup([-1,0,0,0,0,3,3]))