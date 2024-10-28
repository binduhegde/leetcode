def check_perfect_num(num):
    # sm = 0
    # for i in range(1, num//2+1):
    #     if num % i == 0:
    #         sm += i
    #         if sm > num: return sm
    
    # return sm == num

#this takes a lot less time
    if num == 1: return False
    sm = 1
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            sm += i + (num//i)
    return sm == num



print(check_perfect_num(28))