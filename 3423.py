def maxAdjacentDistance(nums) -> int:
    result = 0
    for i in range(0, len(nums)-1):
        result = max((result, abs(nums[i]-nums[i+1])))

    return max((result, abs(nums[0] - nums[-1])))
