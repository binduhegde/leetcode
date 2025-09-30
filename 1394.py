from collections import Counter


class Solution:
    def findLucky(self, arr) -> int:
        # get the frequencies of all the items in arr
        freq = Counter(arr)
        # initialise result with -1
        # which is the default output if no lucky integer is founf
        result = -1

        # Go through the freq dict and if the key == value and
        # the key is more than the currect result, update it.
        for key, value in freq.items():
            if key == value:
                result = max((result, key))
        return result
