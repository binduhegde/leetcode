def zigzag(s, numRows):
    ind = 0
    lst = ['' for i in range(numRows)]
    while ind != len(s):
        for i in range(numRows):
            if ind == len(s): break
            lst[i] +=s[ind]
            ind+=1
        for i in range(numRows-2, 0, -1):
            if ind == len(s): break
            lst[i] +=s[ind]
            ind+=1
    return ''.join(lst)   
    
print(zigzag("PAYPALISHIRING", 3))
