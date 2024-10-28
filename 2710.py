def remove_trailing_zeros(num):
    if num[-1] != '0': return num
    count = 0
    for i in range(len(num)-1, 0, -1):
        if num[i] != '0': break
        count += 1
    return num[:-count]

print(remove_trailing_zeros("51230100"))