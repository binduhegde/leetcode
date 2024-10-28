def merge_sort(nums):
    if len(nums) == 1: return nums
    
    half_ind = len(nums)//2
    left, right = nums[:half_ind], nums[half_ind:]
    merge_sort(left)
    merge_sort(right)
    
    left_ind, right_ind, i = 0,0,0
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            nums[i] = left[left_ind]
            left_ind += 1
        else:
            nums[i] = right[right_ind]
            right_ind += 1
        i += 1
    while left_ind < len(left):
        nums[i] = left[left_ind]
        left_ind += 1
        i += 1

    while right_ind < len(right):
        nums[i] = right[right_ind]
        right_ind += 1
        i += 1
    return nums

print(merge_sort([7,2,6,4,5,1,0,3]))