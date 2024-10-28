def count_pals(string):
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)): 
            if string[i:j+1] == string[i:j+1][::-1]:
                count+=1
                #print(string[i:j])
    return count

print(count_pals('abc'))
print(count_pals('aaa'))
print(count_pals('aba'))
