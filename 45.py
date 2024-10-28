#inp1 = [2,3,1,1,4]
inp = [2,0,3,2,2,0,1,5]
def jump_game(nums):
    l = len(nums)
    lst = [l for _ in range(l)]
    lst[-1] = 0
    
    for i in range(l-2, -1, -1):
        start = i+1
        end = min(i+(nums[i]+1), l)
        if start == end:
            continue
        lst[i] = min(lst[i+1:end])+1
    return lst[0]
print(jump_game(inp))










    # right = len(nums)-1
    # jumps = 0
    # i = 0
    # while right != 0:
    #     if i + nums[i] >= right:
    #         right = i
    #         jumps += 1
    #         i = 0
    #     else: i+=1 
    # return jumps
