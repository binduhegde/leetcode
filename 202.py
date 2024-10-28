def isHappy(n):
    if n == 1: return True
    elif n <= 9: return False
    return isHappy(sum([int(i)**2 for i in str(n)]))

print(isHappy(10))