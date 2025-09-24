class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ---------BRUTE FORCE METHOD-----------
        # ----------O(n*m)---------------------
        # return list(set([i for i in nums1 if i in nums2]))

        # ----------MOST EFFICIENT METHOD----------
        # -----------O(n+m)-----------------------
        # convert both lists to sets to remove duplicates.
        # also, the time complexity for seeing if an item exists in a set is typically O(1) on average,
        # due to the underlying hash table implementation of sets in Python.
        # Hence, making use of sets instead of lists
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return [i for i in nums1_set if i in nums2_set]
