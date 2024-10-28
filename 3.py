def lengthOfLongestSubstring(s):
    lengths = 0
    substr = ''
    for i in s:
        for char in range(len(substr)):
            if substr[char] ==i:
                if len(substr) > lengths: lengths = len(substr)
                substr = substr[char+1:]
                break
        substr += i
    return lengths

print(lengthOfLongestSubstring('abcabcbb'))
