def binary_search(nums, t):
    l, r = 0, len(nums)
    middle = len(nums)//2
    while l != r:
        if nums[middle] == t:
            return middle
        elif nums[middle] > t:
            r = middle
        else:
            l = middle+1
        middle = (l+r) // 2

    return -1
print(binary_search([5], 5))
                    # 0 1 2 3 4 5