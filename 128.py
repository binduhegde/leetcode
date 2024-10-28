def longest_con(nums):
    nums = set(nums)
    longest = 0

    for i in nums:
        if i - 1 not in nums:
            length = 0
            while i + length in nums:
                length += 1
            longest = max(longest, length)
    return longest

# when searching for the existence of a value in set, 
# it takes O(1) time. Didn't fully understand how