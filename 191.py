def hamming_weight(n):
    binary = str(bin(n))[2:]
    
    return len([i for i in binary if i == '1'])

print(hamming_weight(11))