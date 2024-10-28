def num_squares(n):
    squares = [i**2 for i in range(1, int(n**0.5)+1)]
    
    dp = [n+1] * (n+1)
    dp[0] = 0
    for num in range(1, n+1):
        for square in squares:
            if num - square >= 0:
                dp[num] = min(dp[num], 1+dp[num-square])
    return dp[-1]

print(num_squares(12))
