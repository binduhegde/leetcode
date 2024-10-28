n = [1,3,4,1,2,3,1]

def findMatrix(nums):
    if len(nums) == 0: return []
    result =[list(set(nums))]
    for i in result[0]:
        nums.remove(i)
    return result + findMatrix(nums)

print(findMatrix(n))

a = 'aabcd'
a = a.replace('a', 'z',1)
print(a)