def count_ast(s):
    count = 0
    ok = True
    for i in s:
        if i == '|':
            ok = True if ok == False else False
        if ok is True and i == '*':
            count += 1
    return count
            
print(count_ast("l|*e*et|c**o|*de|"))
print(count_ast("yo|uar|e**|b|e***au|tifu|l"))