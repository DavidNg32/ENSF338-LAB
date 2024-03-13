import sys

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

operands = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
} # Operands

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(expression):
    tokens = expression.split()
    print(tokens)
    stack = []
    parent = None
    for token in tokens:
        if token == ')':
            right = stack.pop()
            parent = stack.pop()
            left = stack.pop()
            parent.left = left
            parent.right = right
            stack.append(parent)
            continue
        elif token.isdigit():
            stack.append(Node(int(token)))
        elif token in '+-*/':
            node = Node(token)
            stack.append(node)
    if len(stack) == 3: # if there are 3 elements in the stack would mean the right side of the tree is not complete as it ends with a constant
        right = stack.pop()
        parent = stack.pop()
        left = stack.pop()
        parent.left = left
        parent.right = right
        stack.append(parent)

    return stack[-1]

def postorder(node):
    if node:
        left = postorder(node.left)
        right = postorder(node.right)
        if node.value in operands:
            print(f'left: {left} right: {right} node: {node.value}')
            result = int(operands[node.value](left, right))
            print(f'result: {result}')
            return int(operands[node.value](left, right))
        else:
            return node.value
def main():
    expression = sys.argv[1]
    root = build_tree(expression)
    print(postorder(root))

if __name__ == "__main__":
    main()