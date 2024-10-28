n = [4,6,5,9,3,7]
left = [0,0,2]
right = [2,3,5]

def checkArithmeticSubarrays(nums, l, r):
    answer = []
    for index in range(len(l)):
        seq = sorted(nums[l[index]: r[index]+1])
        diff = seq[1] - seq[0]
        
        for i in range(2, len(seq)):
            if seq[i] - seq[i-1] != diff:
                answer.append(False)
                break
        else: answer.append(True)
    return answer

print(checkArithmeticSubarrays(n, left, right))        