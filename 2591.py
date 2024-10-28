def dist_money(money, children):
    if money < children: return -1
    lst = [0 for i in range(children)]
    for i in range(children):
        if i == children-1:
            lst[i] = money
        elif money >= 8 and money-8 !=4 and money-8 >= children-i-1:
            lst[i] = 8
            money -= 8
        else: 
            lst[i] = 1
            money -= 1
    print(lst)
    leng = len([i for i in lst if i == 8])
    if leng != 0: return leng
    return -1 

print(dist_money(20, 3))