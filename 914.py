from collections import Counter

def divide_cards(deck):
    counts = sorted(set(list(dict(Counter(deck)).values())))
    first = counts[0]
    if first < 2: return False
    for i in range(2, first+1):
        for item in counts:
            if item % i != 0:
                break
        else: return True
    return False


# print(divide_cards([1,2,3,4,4,3,2,1]))
# print(divide_cards([1,1,1,1,2,2,2,2,2,2]))