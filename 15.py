def three_sum(nums):
    nums = sorted(nums)
    result = []
    for i in range(len(nums)):
        target = -1 * nums[i]
        l, r = i+1, len(nums)-1
        while r>l:
            added = nums[l]+nums[r]
            if added < target:
                l += 1
            elif added > target:
                r -= 1
            else:
                sorted_trip = sorted([nums[i], nums[l], nums[r]])
                if sorted_trip not in result:
                    result.append(sorted_trip)
                l, r = l+1, r-1
    return result

print(three_sum([-1,0,1,2,-1,-4]))