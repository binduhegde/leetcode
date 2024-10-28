def balance_str(s):
    output = 0
    count_r = 0
    count_l = 0
    for i in s:
        if i == 'L': count_l +=1
        else: count_r +=1
        if count_l == count_r: 
            output+= 1
            count_l, count_r = 0, 0
    return output

print(balance_str("RLRRLLRLRL"))