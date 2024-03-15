import heapq
import random
import timeit

class ListNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, data, priority):
        NewNode = ListNode(data, priority)
        if not self.head or self.head.priority > priority:
            NewNode.next = self.head
            self.head = NewNode
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            NewNode.next = current.next
            current.next = NewNode

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data
    
class HeapPriorityQueue:#copilot used for heapq
    def __init__(self):
        self.heap = []

    def enqueue(self, data, priority):
        heapq.heappush(self.heap, (priority, data)) #copilot

    def dequeue(self):
        if not self.heap:
            return None
        priority, data = heapq.heappop(self.heap)
        return data

def randtasks():
    tasks = []

    for _ in range(1000):
        random_number = random.random()
        tasks.append(("enqueue", random.randint(1, 100)) if random_number < 0.7 else ("dequeue",None))

    return tasks

tasks = randtasks()

listpq = ListPriorityQueue()
timepq = timeit.timeit(lambda: [listpq.enqueue(task[1], random.randint(1, 100)) if task[0] == 'enqueue' else listpq.dequeue() for task in tasks], number=1)
avg = timepq / 1000

print("ListPriorityQueue:")
print("Overall Time:", timepq)
print("Average Time per Task:", avg)

heappq = HeapPriorityQueue()
timepq = timeit.timeit(lambda: [heappq.enqueue(task[1], random.randint(1,100)) if task[0] == 'enqueue' else heappq.dequeue() for task in tasks], number=1)
avg = timepq / 1000

print("HeapPriorityQueue:")
print("Overall Time:", timepq)
print("Average Time per Task:", avg)

print("The HeapPriorityQueue is faster according to the times above")
print("This is because of the time complexity of their fundamental operations. HeapPriorityQueue has enqueue and dequeue which has")
print("a time complexity of O(logn), but for the other implementation, the time complexity is O(n).")