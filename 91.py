from functools import cache


def n_decoding(s):
    # @cache works ONLY if you're using python 3.9 + versions
    @cache
    def dp(i):
        # base case 1: we've reached the end of the string
        if len(s) <= i:
            return 1
        # base case 2: the first digit is 0
        elif s[i] == '0':
            return 0

        if i < len(s)-1 and int(s[i:i+2]) <= 26:
            return dp(i+1) + dp(i+2)
        else:
            return dp(i+1)
    return dp(0)


print(n_decoding('26'))
