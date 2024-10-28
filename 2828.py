def check_acrony(w, s):
    # if len(w) != len(s): return False
    # for i in range(len(s)):
    #     print(s[i][0], s[i])
    #     if w[i][0] != s[i]: return False
    # return True
    return ''.join([i[0] for i in w]) == s

print(check_acrony(["alice","bob","charlie"], "abc"))
print(check_acrony(["afqcpzsx","icenu"], 'yi'))