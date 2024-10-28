#wrong
def min_speed(piles, h):

    piles.sort(reverse= True) #[11, 7, 6, 3]
    if len(piles)*2 -1 >= h:
        if piles[h-len(piles)]*2 >= piles[0]:
            return piles[h-len(piles)]
    
    summ = sum(piles)
    least = int(summ/h) + (summ % h >0)
    return least
    while True:
        c = 0
        for i in piles:
            c += int(i/least) + (i % least > 0)
        if c <= h: break
        least += 1
    return least
        
print(min_speed([1,1,1,999999999], 10))
print(999999999/10)
