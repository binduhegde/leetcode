def power_of_two(n):
    if n <= 1: return False
    while n % 2 == 0 and n != 2: n = n//2
    return n == 2

print(power_of_two(8))
