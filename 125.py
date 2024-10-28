def valid_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s

print(valid_palindrome("A man, a plan, a canal: Panama"))