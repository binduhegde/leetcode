def smallest_pal(s):
    s = list(s)
    for i in range(int(len(s)/2)):
        s1, s2 = s[i], s[-1*(i+1)]
        if s1 == s2: continue
        elif ord(s1) > ord(s2):
            s[i] = s2
        else:
            s[-1*(i+1)] = s1
    return ''.join(s)

print(smallest_pal('abcda'))

