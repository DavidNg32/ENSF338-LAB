import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
        else:
            return None

def operations(a, b):

    if '+':
        return a + b
    
    elif '-':
        return 


expression = sys.argv[1]

if __name__ == "__main__":
    stack = Stack()
    for i in expression:
        if i.isdisgit() or i in operations:
            stack.push(i)
        elif i == ')':
            b = stack.pop()
            a = stack.pop()
            op = stack.pop()
            stack.push(operations(op)(int (a), int (b), ))
