from collections import Counter
def minSteps(s, t):
    # for i in s:
    #     if i in t:
    #         t = t.replace(i, '', 1)
    # return len(t)
    cnt1=Counter(s)
    cnt2=Counter(t)
    sm=0
    for i,j in cnt2.items():
        if i in cnt1 and j>cnt1[i]:
            sm+=abs(j-cnt1[i])
        elif i not in cnt1:
            sm+=j
    return sm
print(minSteps('aab', 'abc'))
print(minSteps('leetcode', 'practice'))