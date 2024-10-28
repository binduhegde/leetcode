def total_money(n):
    total = 0
    for i in range(n//7):
        total += 28 + (i*7)
    pos = (n//7)
    for j in range(pos+1, pos+1+(n%7)):
        total += j
        print(j, total)
    return total

print(total_money(4))