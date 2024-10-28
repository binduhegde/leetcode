def get_pattern(pattern):
    d = {pattern[0]:0}
    lst = []
    ind = 1
    for i in range(len(pattern)):
        if pattern[i] not in d.keys():
            d[pattern[i]] = ind
            ind +=1
        lst.append(d[pattern[i]])
    return lst


def find_replace_pattern(words, pattern):
    p = get_pattern(pattern)
    output = [word for word in words if get_pattern(word) == p]
    return output

print(find_replace_pattern(["abc","deq","mee","aqq","dkd","ccc"], 'abb'))


