p1 = [7,1,5,3,6,0]
p2 = [7, 5, 18, 1, 7]
p3 = [5,4,3,2,1]
p4 = [1]

def max_profit(prices): 
    if len(prices) <= 1: return 0
    mini = [0, prices[0]]
    maxi = [0, 0]
    for i in range(len(prices)):        
        if prices[i] < mini[1] and i != len(prices)-1:
            mini = [i, prices[i]]
        if prices[i] > maxi[1] and i > mini[0] and i != 0:
            maxi = [i, prices[i]]
    max_min = max(prices[mini[0]:]) - mini[1]
    min_max = maxi[1] - min(prices[:maxi[0]])
    max_of_two = max([max(max_min, min_max), 0])
    return max_of_two

print(max_profit(p4))