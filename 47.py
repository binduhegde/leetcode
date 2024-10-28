def permute(nums): 
    result = []

    # if there is only one element in the nums, i.e., if we have reached 
    # the end of recursion, it only return that number in a list of list
    if len(nums) == 1:
        return [nums[:]]
    
    for i in range(len(nums)):
       
        # removes the first value to add it later
        n = nums.pop(0) 
        
        # keeps recursing until there's only one item in the list
        perms = permute(nums)
        
        for perm in perms:
            # to the permutation, adds the char which we popped before
            perm.append(n)
            
            # makes sure there is no duplication of items
            if perm not in result:
                result.append(perm)
        
        # retrieves the value we popped before
        nums.append(n)
    
    return result

print(permute([1,1,3]))