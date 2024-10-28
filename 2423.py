def word_fre(word):
    word_freq ={}
    for i in word:
        word_freq[i] = word_freq.get(i, 0)+1

    
    for key, value in word_freq.items():
        temp = word_freq.copy()
        if temp[key] == 1: del temp[key]
        else: temp[key] -= 1
        if len(set(list(temp.values()))) == 1: return True
    return False


print(word_fre("bac"))