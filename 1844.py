def replace_digits(s):
    for i in range(1, len(s), 2):
        s = s.replace(s[i], chr(ord(s[i-1])+int(s[i])),1)
    return s

print(replace_digits("a1c1e1"))

a = "a1c1e1"
a.replace('1', 'b', 1)
print(a)