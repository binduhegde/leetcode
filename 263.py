# def prime_factor(n):
#     if n < 2: return 1
#     for i in range(2, n+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             if n % i == 0:
#                 return i

# def is_ugly(n):
#     while n != 1:
#         factor = prime_factor(n)
#         if factor not in [2, 3, 5]: return False
#         n = n // factor

#     return True



def is_ugly(n):
    if n == 0: return False
    while n != 1:
        if n % 2 == 0: n /= 2
        elif n % 3 == 0: n /= 3
        elif n % 5 == 0: n /= 5
        else: return False
    return True

print(is_ugly(10))