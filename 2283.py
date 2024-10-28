from collections import Counter

def digitCount(num):
    for i in range(len(num)):
        if int(num[i]) != num.count(str(i)):
            return False
    return True

print(digitCount('1210'))

