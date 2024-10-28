s = ["eat","tea","tan","ate","nat","bat"]

def group_anagrams(strs): 
    lst = [''.join(sorted(a)) for a in strs]
    dicti = {i:[] for i in lst}
    for i in range(len(strs)):
        dicti[lst[i]].append(strs[i])
    return list(dicti.values())

print(group_anagrams(s))