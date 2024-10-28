def kth_factor(n, k):
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i != 0:
            continue
        factors.append(i)
        factors.append(n//i)
    
    factors = sorted(set(factors))

    return -1 if k > len(factors) else factors[k-1]


print(kth_factor(4, 4))
