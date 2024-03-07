import random
import timeit
import matplotlib.pyplot as plt

#Question 1
class ArrayStack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if not self.stack:
            return None
        else:
            return self.stack.pop()
    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]
        
#Question 2
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

class ListStack:
    def __init__(self):
        self.head = None
    def push(self, value):
        node = Node(value)
        node.setNext(self.head)
        self.head = node
    def pop(self):
        if self.head is None:
            return None
        returnvalue = self.head.getData()
        self.head = self.head.getNext()
        return returnvalue
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.getData()
        
#Question 3
def randtasks():
    tasks = []

    for _ in range(10000):
        random_number = random.random()
        tasks.append("push" if random_number < 0.7 else "pop")

    return tasks

#Question 4
def execution(impl, tasks):
    stack = impl()
    for task in tasks:
        if task == "push":
            stack.push(1)
        elif task == "pop":
            stack.pop()

arraytimes= []
lltimes = []
for i in range(100):
    tasks = randtasks()

    time_taken = timeit.timeit(lambda: execution(ListStack, tasks), number=1)
    lltimes.append(time_taken)
    time_taken = timeit.timeit(lambda: execution(ArrayStack, tasks), number=1)
    arraytimes.append(time_taken)

print("ArrayStack average time:", sum(arraytimes) / len(arraytimes))
print("LinkedListStack average time:", sum(lltimes) / len(lltimes))
print("Implementing an array stack is much more efficient than implementing a Linked List stack.")
plt.hist(arraytimes, bins=5, alpha=0.5, label='ArrayStack')
plt.hist(lltimes, bins=5, alpha=0.5, label='LinkedListStack')
plt.xlabel('Time Taken')
plt.ylabel('Frequency')
plt.title('Distribution of Execution Times')
plt.legend()
plt.show()