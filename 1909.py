def check_inc(nums):
    for i in nums:
        temp = nums[:]
        temp.remove(i)
        for j in range(1, len(temp)):
            if not temp[j] > temp[j-1]:
                return False
    return True
print(check_inc([541,783,433,744]))
#THIs is incomplete