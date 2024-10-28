def rob(nums):
    if len(nums) == 0: return 0
    elif len(nums) == 1: return nums[0]
    elif len(nums) == 2: return max(nums[0], nums[1])
    dp = [0] * (len(nums)+1)
    dp[-2], dp[-3] = nums[-1], max(nums[-1], nums[-2])
    for i in range(len(nums)-3, -1, -1):
        dp[i] = nums[i]+ max(dp[i+2], dp[i+3])
    return max(dp[0], dp[1])



print(rob([9,1,2,9,3,4]))
print(rob([2,7,9,3,1]))
print(rob([1,6,3]))
