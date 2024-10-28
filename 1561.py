def max_coins(piles):
    piles = sorted(piles)
    count = 0
    times = len(piles) // 3
    for i in range(times, len(piles), 2):
        count += piles[i]
    return count

print(max_coins([2,4,1,2,7,8]))
print(max_coins([9,8,7,6,5,1,2,3,4]))
a = 'avdv'
print(a[::-1])