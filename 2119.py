def same_after_reverse(n):
    #return n == int(str(int(str(n)[::-1]))[::-1])
    if str(n)[-1] == '0' and n != 0: return False
    return True
print(same_after_reverse(180))