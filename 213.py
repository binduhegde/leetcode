def rob(nums):
    if len(nums) <= 3: return max(nums)

    # there are two ways we can do this. one is to rob the last house and leave the first one. 
    # second option is to rob the first house and leave the last one. 

    case_one, case_two = [0]* (len(nums)+1), [0]* len(nums)
    case_one[-2], case_one[-3] = nums[-1], max(nums[-1], nums[-2]) #[0, 0, 0, 0, 9, 8, 0]
    case_two[-2], case_two[-3] = nums[-2], max(nums[-2], nums[-3]) #[0, 0, 0, 9, 9, 0]
    for i in range(len(nums)-3, 0, -1):
        case_one[i] = nums[i] + max(case_one[i+2], case_one[i+3])
    for j in range(len(nums)-4, -1, -1):
        case_two[j] = nums[j] + max(case_two[j+2], case_two[j+3])
    
    return max(case_one[1], case_one[2], case_two[0], case_two[1])

print(rob([10,8,7,3,9,8]))
