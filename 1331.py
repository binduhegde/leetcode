def rank(arr):
    sorted_arr = sorted(list(set(arr)))

    op = []
    for i in arr:
        op.append(sorted_arr.index(i)+1)
    return op


print(rank([40,10,20,30,30]))