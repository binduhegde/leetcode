def twoOutOfThree(nums1, nums2, nums3):
    # creating a set of nums1 because the duplicates don't matter
    # and the time complexity to search an element in set is O(1)
    nums1set = set(nums1)
    # creating nums2set to compare it with nums3
    nums2set = set(nums2)
    # again, creating a result set where the items in the result will be added
    # along with the result list. Creating a separate set,
    # again because of the time complexity to search in a list is O(1)
    result_set = set()
    result = []

    # 3 rounds of for loops to cover all list combinations
    # all the combinations: nums1 vs nums2, nums1 vs nums3 and nums2 vs nums3

    # to cover nums1 vs nums2
    for num in nums2:
        # if the number exists in the other list
        # and hasn't already been added to the result
        if num in nums1set and num not in result_set:
            result_set.add(num)
            result.append(num)

    # nums1 vs nums3
    for num in nums3:
        # if the number exists in the other list
        # and hasn't already been added to the result
        if num in nums1set and num not in result_set:
            result_set.add(num)
            result.append(num)

    # nums2 vs nums3
    for num in nums3:
        # if the number exists in the other list
        # and hasn't already been added to the result
        if num in nums2set and num not in result_set:
            result_set.add(num)
            result.append(num)

    return result


print(twoOutOfThree([1, 1, 3, 2], [2, 3], [3]))
