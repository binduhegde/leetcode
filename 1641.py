def convert_vowel(n):
    mul=1
    j=1
    for i in range(5,5+n):
        mul=(mul*i)//j
        j+=1
    return mul

for i in range(20):
    print(i, convert_vowel(i))