def dia_sum(mat):
    added = 0
    left = 0
    for lst in mat:
        added += lst[left]
        added += lst[-1-(left)]
        left +=1
    if len(mat) % 2 != 0:
        added -= mat[(len(mat)//2)][(len(mat)//2)]
    return added

print(dia_sum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]))