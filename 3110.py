def score(s):
    ascii_values = [ord(i) for i in s]
    
    diff = [abs(ascii_values[i] - ascii_values[i+1]) for i in range(len(ascii_values)-1)]
    return sum(diff)

print(score('hello'))