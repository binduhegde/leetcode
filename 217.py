#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:31:50 2023

@author: bindu
"""
from typing import List

class Solution:
    
    # O(n^2) time and O(1) space
    def solution1(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    # O(n) time and O(n) space
    def solution2(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            nums_set.add(i)
        return False

    # sort the list and it brings the duplicates together
    # we can compare the adjacent elements to check
    # O(n logn) time and O(1) space
    def solution3(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.solution2(nums)
    