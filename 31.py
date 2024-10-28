# all changes are to be done in place. returns nothing
def next_permutation(nums):
    # nothing to do if there is only one value in nums
    if len(nums) == 1: return 

    # if the last two elements are in ascending order, 
    # swap them. eg: 123 becomes 132
    elif nums[-1] > nums[-2]:
        nums[-1], nums[-2] = nums[-2], nums[-1]
        return

    # break_point is the index of the nums list where we have to swap a 
    # number at that index with another in the right side of the nums list. 
    # How we find break_point is that we go from the list in reverse order 
    # (right to left) and mark the point where it's not ascending 
    # anymore(acsending from right to left)
    # eg: for nums = [1,4,5,8,7], 5 is the break_point because 
    # 7 is less than 8 but 8 isn't less than 5
    break_point = None
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums [i+1]:
            break_point = i
            break
    
    # break_point remains None when the array is in descending order
    # in which case we reverse the array. 321 becomes 123 and that's the ans
    if break_point == None:
        nums.reverse()
        return
    
    # once we've found the break_point, we need to decide which number 
    # should come in the place of break_point. it should be in the 
    # right side of the array and it should be greater than what's 
    # already at the break_point index because anything less than than 
    # has already come before this permutation. Here, we take the smallest 
    # number we can find in the right side of the array which is still 
    # greater than nums[break_point]
    smallest_ind = None
    for j in range(break_point, len(nums)):
        if nums[j] > nums[break_point]:
            if smallest_ind is None:
                smallest_ind = j
            elif nums[smallest_ind] > nums[j]:
                smallest_ind = j
    
    # here we swap that value with whatever's there in nums[break_point]
    nums[break_point], nums[smallest_ind] = nums[smallest_ind], nums[break_point]

    # hence this is a new value for the break_point place, 
    # we sort the right side of the array
    nums[break_point+1:] = sorted(nums[break_point+1:])


lst = [1,4,5,8,7]
next_permutation(lst)
print(lst)
