def count_char(words, chars):           
    result = []
    for word in words:
        chrs = chars[::]
        for chr in word:
            if chr not in chrs:
                break
            chrs = chrs.replace(chr, '', 1)
        else:
            result.append(word)
    return len(''.join(result))

print(count_char(["cat","bt","hat","tree"], "atach"))