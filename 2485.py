import math 
def find_pivot(n):
    N = n* (n+1)//2
    k = math.isqrt(N)
    return k if N == k*k else -1   

for i in range(1000): 
    pivot = find_pivot(i)
    if pivot != -1:
        print(i, pivot)
