def longest_palindrome(s):  
    palindrome = ''
    for i in range(len(s)):
        substr = s[i]
        for j in range(i+1, len(s)):
            substr+= s[j]
            if substr == substr[::-1] and len(palindrome) < len(substr):
                palindrome = substr
    if len(palindrome) == 0: return s[0]
    return palindrome

print(longest_palindrome('m'))