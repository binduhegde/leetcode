def sort_vowels(s):
    s = list(s)
    lst = [[i, ord(s[i])] for i in range(len(s)) if s[i].lower() in ['a', 'e', 'i', 'o', 'u']]
    sorted_lst = sorted(list(map(lambda x:x[1], lst)))
    for i in range(len(lst)):
        print(s[lst[i][0]], chr(sorted_lst[i]))
        s[lst[i][0]] = chr(sorted_lst[i])
    return ''.join(s)
print(sort_vowels("lEetcOde"))
