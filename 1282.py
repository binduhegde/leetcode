def groupThePeople(groupSizes): 
    dicti = {i:[[]] for i in set(groupSizes)}

    for i in range(len(groupSizes)):
        dicti[groupSizes[i]][0].append(i)

    for key, value in dicti.items():
        if len(value[0]) > key:
            
            temp_value = value[:]
            dicti[key] = []
            
            for i in range(key, len(temp_value[0]), key):
                print(i)
                dicti[key].append(temp_value[0][:key])
                temp_value = [temp_value[0][key:]]
            dicti[key].append(temp_value[0])
    return sum([value for value in dicti.values()],[])

#print(groupThePeople([2,1,3,3,3,2,2,2,3]))
#print(groupThePeople([2,2,1,1,1,1,1,1]))
print(groupThePeople([3,3,3,3,3,1,3]))
