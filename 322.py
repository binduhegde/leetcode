def coin_change(coins, amount):
    # we first have to calculate for every number till the amount.
    # dp stores all the min values for every number
    # [amount + 1] is to just set every number to the highest. can also set it to infinity
    dp = [amount + 1] * (amount+1)
    dp[0] = 0 # to make the sum 0, we need minimum of 0 coins
    
    for amt in range(1, amount+1):
        for coin in coins:
            if amt - coin >= 0: # this runs onlt if the current amt can be made up by some combination
                # this stores the min value between itself and 1+dp[amt-coin]
                # since we're calculating from 0-n, dp[amt-coin] value should already exist. 
                # plus 1 is the current coin we're adding
                dp[amt] =  min(dp[amt], 1+dp[amt-coin])
    #if dp[amount] can not be made up by any combination, it'd still have its default value i.e., amount + 1
    return dp[amount] if dp[amount] != amount + 1 else -1

print(coin_change([1,3,4,5], 7)) # and is 2 i.e., coin [3, 4]
#print(coin_change([1,2,8,10], 24))