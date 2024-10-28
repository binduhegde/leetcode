def reverse_string(s, k):
    reverse = ''
    for i in range(0, len(s), 2):
        if i % (k*2) == 0:
            if i + 2 > len(s):
                reverse += s[i:][::-1]
            else: reverse += s[i:i+k][::-1]
        else: reverse += s[i:i+k]
    return reverse

print(reverse_string("abcdefghi", 2))