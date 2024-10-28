def check_pangram(s):
    dicti= {i:0 for i in range(97, 123)}
    for i in s:
        dicti[ord(i)] = 1
    for k, v in dicti.items():
        if v == 0: return False
    return True

print(check_pangram("thequickbrownfoxjumpsoverthelazydog"))