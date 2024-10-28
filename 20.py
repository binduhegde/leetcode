def valid_paratheses(s):
    valid = {'(': ')', '[': ']', '{': '}'}
    opening = ['(', '[', '{']
    if s[0] not in opening: return False
    to_close = [valid[s[0]]]
    for i in range(1, len(s)):
        if s[i] not in opening:
            if len(to_close) == 0 or s[i] != to_close[-1]: return False
            else:
                to_close.pop(-1)
        else:
            to_close.append(valid[s[i]])
    return len(to_close) == 0


print(valid_paratheses("()[]{}"))
print(valid_paratheses('([)])'))
print(valid_paratheses("{[]}"))
print(6/-132)