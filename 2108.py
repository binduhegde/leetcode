def firstPalindrome(words):
    for i in range(len(words)):
        if words[i] == words[i][::-1]:
            return i
    return ""
    

print(firstPalindrome(["abc","car","ada","racecar","cool"]))
