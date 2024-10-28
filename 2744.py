def pair_strings(words): 
    taken = []
    count = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if j in taken: continue
            if words[i][::-1] == words[j]:
                count +=1
                taken.append(j)
    return count

print(pair_strings(["cd","ac","dc","ca","zz"]))