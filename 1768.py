def merge_alt(word1, word2):
    result = ''
    if len(word1) < len(word2):
        s, l = word1, word2
    else: s, l = word2, word1
    for i in range(len(s)):
        result += word1[i] + word2[i]
    result += l[i+1:]
    return result

print(merge_alt('ace', 'bdf'))