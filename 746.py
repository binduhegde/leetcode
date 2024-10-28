def climb_stairs(cost):
    dp = [cost[-1], cost[-2]]
    for i in range(len(cost)-3, -1, -1):
        dp.append(cost[i]+ min(dp[-1], dp[-2]))
    return min(dp[-1], dp[-2])

print(climb_stairs([1,100,1,1,1,100,1,1,100,1]))