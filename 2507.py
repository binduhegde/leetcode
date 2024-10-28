def prime_till_n(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i**2, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]
#print(prime_till_n(8))

def smallest_value(n):
    if n == 4: return 4
    prime = prime_till_n(n)
    factors = []
    
    while n != 1:
        for i in range(len(prime)):
            if n % prime[i] == 0:
                n = n//prime[i]
                factors.append(prime[i])
                break
    if len(factors) != 1:
        return smallest_value(sum(factors))
    return factors[0]
print(smallest_value(3))