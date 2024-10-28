def count_primes(n):
    # if n < 2: return 0
    # elif n < 5: return n-2
    # count = 1
    # for num in range(3, n):
    #     for i in range(2, num//2):
    #         if num % i == 0:
    #             break
    #     else:
    #         count +=1
    # return count-1
    if n < 2: return 0

    primes = [True] * n
    primes[0], primes[1] = False, False

    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False

    return sum(primes)
        

print(count_primes(10))

