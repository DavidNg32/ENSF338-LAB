# ex4 JJD
import random
import timeit
import matplotlib.pyplot as plt

class queueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.checkEmpty():
            return None  
        return self.queue.pop()

    def checkEmpty(self):
        return len(self.queue) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queueLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.checkEmpty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.checkEmpty():
            return None  
        dequeued_item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_item

    def checkEmpty(self):
        return self.head is None
    
def randomTasks():
    tasks = []
    for _ in range(10000):
        if random.random() < 0.7:
            tasks.append('enqueue')
        else:
            tasks.append('dequeue')
    return tasks

array_setup = '''
from __main__ import queueArray
queue = queueArray()
'''

linked_list_setup = '''
from __main__ import queueLinked
queue = queueLinked()
'''

code = '''
for task in tasks:
    if task == 'enqueue':
        queue.enqueue(1)
    else:
        queue.dequeue()
'''

# Time queueArray
arrayTimes = [timeit.timeit(code, setup=array_setup, globals={'tasks': randomTasks()}, number=1) for _ in range(100)]

# Time queueLinked
linkedListTimes = [timeit.timeit(code, setup=linked_list_setup, globals={'tasks': randomTasks()}, number=1) for _ in range(100)]

print("queueArray average time:", sum(arrayTimes) / len(arrayTimes))
print("queueLinked average time:", sum(linkedListTimes) / len(linkedListTimes))

#Plotting code
plt.hist(arrayTimes, bins=10, alpha=0.5, label='queueArray')
plt.hist(linkedListTimes, bins=10, alpha=0.5, label='queueLinked')
plt.xlabel('Time to execute (sec.)')
plt.ylabel('Frequency')
plt.title("Execution Times' Distribution")
plt.legend(loc='upper right')
plt.show()
