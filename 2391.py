g = ["G","P","GP","GG"] 
t = [2,4,3]

def garbage_collection(garbage, target):
    garbage_dict = {'G': [0, 0], 'P': [0, 0], 'M': [0, 0]}
    for i in range(len(garbage)):
        for j in garbage[i]:
            garbage_dict[j][0] += 1
            garbage_dict[j][1] = i

    added = 0
    for value in garbage_dict.values():        
        added += sum(target[:value[1]]) + value[0]
    return added

print(garbage_collection(g, t))
print(-1%2)