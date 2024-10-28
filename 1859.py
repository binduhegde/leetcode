def sort_sentence(s): 
    s = s.split()
    l = ['' for i in range(len(s))]
    for word in s:
        l[int(word[-1])-1] = word[:-1]
    return ' '.join(l)

print(sort_sentence("is2 sentence4 This1 a3"))