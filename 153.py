def find_min(nums):
    lowest= nums[0]
    left_ind = 0
    right_ind = len(nums) - 1

    while left_ind <= right_ind:
        if nums[left_ind] < nums[right_ind]:
            lowest = min(lowest, nums[left_ind])
            break

        middle_ind = (left_ind+right_ind) // 2
        lowest = min(lowest, nums[middle_ind])
        if nums[middle_ind] >= nums[left_ind]:
            left_ind = middle_ind + 1
        else:
            right_ind = middle_ind -1
    return lowest


print(find_min([3,4,5,1,2]))
print(find_min([3,1,2]))
print(find_min([1]))