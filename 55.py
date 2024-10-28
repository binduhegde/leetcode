def jump_game(nums):
    right = len(nums) - 1
    for i in range(len(nums)-2,-1,-1):
        if i + nums[i] >= right:
            right = i
    return right == 0

print(jump_game([0]))
print(jump_game([2,3,1,1,4]))
print(jump_game([3,2,1,0,4]))