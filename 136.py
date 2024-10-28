def singleNumber(nums: list[int]) -> int:
        n = 0

        for num in nums:
            n ^= num

        return n

#print(singleNumber([2,2,1]))
print(singleNumber([4,2,1,1,2]))