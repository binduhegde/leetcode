inp = [1,4,2,5,7,8,1, 2]

def sum_off_len(arr):
    # total = 0
    # n = [i for i in range(1, len(arr)+1, 2)]
    # for length in n:
    #     for i in range(len(arr)):
    #         if i+length > len(arr): break
    #         total += sum(arr[i:i+length])
    # return total

    l = len(arr)
    ans = 0
    for i in range(l):
        c = ((i+1)*(l-i)+1)//2
        print(c)
        ans += c * arr[i]
    return ans
print(sum_off_len(inp))