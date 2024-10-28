n = [1,1,1,2,2,3, 4,4,4,4]
def top_k(nums, k):
    dicti = {}
    for i in nums:
        dicti[i] = dicti.get(i, 0)+1
    sorted_dict = sorted(dicti.items(),key = lambda kv: kv[1], reverse=True)
    return [sorted_dict[i][0] for i in range(k)]

print(top_k(n, 2))