
import sys

def parser(expression):
    stack = []
    
    for i in expression:
        if (i != "(") and (i != ' '):
            stack.append(i)
        if i == ')':
            stack.pop()
            secondOperand = stack.pop()
            firstOperand = stack.pop()
            operator = stack.pop()
            result = evaluate(operator, firstOperand, secondOperand)
            stack.append(result)
        else:
            continue
    
    return stack.pop()
    
def evaluate(operator, one, second):
    if operator == '+':
        return int(one) + int(second)
    elif operator == '-':
        return int(one) - int(second)
    elif operator == '*':
        return int(one)*int(second)
    elif operator == '/':
        return int(one)/int(second)
    else:
        raise ValueError("Invalid Equation")

print(parser(sys.argv[1].strip()))