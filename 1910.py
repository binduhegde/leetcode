def remove_occ(s, part):
    while part in s:
        s = s.replace(part, '', 1)
    return s  


print(remove_occ("daabcbaabcbc", 'abc'))