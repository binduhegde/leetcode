def evalRPN(tokens):  
    result = []
    for i in tokens:
        to_append = 0
        if i == '+':
            to_append = result[-1]+result[-2]
        elif i == '-':
            to_append = result[-2] - result [-1]
        elif i == '*':
            to_append = result[-1] * result[-2]
        elif i == '/':
            to_append = int(result[-2]/result[-1])
        else:
            result.append(int(i))
            continue
        result.pop()
        result.pop()
        result.append(to_append)
        
    return result[0]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

