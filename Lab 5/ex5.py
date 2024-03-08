#Question 1
class ArrayQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def isempty(self):
        return self.head == -1

    def isfull(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, data):
        if self.isfull():
            print("Queue is full. Unable to enqueue data.")
            return
        elif self.isempty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = data

    def dequeue(self):
        if self.isempty():
            print("Queue is empty. Unable to dequeue data.")
            return None
        data = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return data

    def peek(self):
        if self.isempty():
            print("Queue is empty. Unable to peek data.")
            return None
        return self.queue[self.head]

#Question 2
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue data.")
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Unable to peek data.")
            return None
        return self.head.data
    
array_queue = ArrayQueue(5)
circular_queue = CircularQueue()

queues = [array_queue, circular_queue]

for queue in queues:
    print("\n" + "-" * 50)
    print(f"Testing {queue.__class__.__name__}")

    # Enqueue operations
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    # Try to enqueue into a full queue
    if isinstance(queue, ArrayQueue):
        queue.enqueue(6)  # Expected output: "Queue is full. Unable to enqueue data."

    print(queue.dequeue())  # Expected output: 1
    print(queue.dequeue())  # Expected output: 2
    print(queue.dequeue())  # Expected output: 3


    queue.enqueue(7)
    queue.enqueue(8)


    print(queue.dequeue())  # Expected output: 4
    print(queue.dequeue())  # Expected output: 5
    print(queue.dequeue())  # Expected output: 7
    print(queue.dequeue())  # Expected output: 8

    # Try to dequeue from an empty queue
    print(queue.dequeue())  # Expected output: "Queue is empty. Unable to dequeue data."

    # Try to peek into an empty queue
    print(queue.peek())  # Expected output: None 

    # Enqueue into an empty queue
    queue.enqueue(9)

    # Dequeue operations
    print(queue.dequeue())  # Expected output: 9

    # Try to dequeue from an empty queue
    print(queue.dequeue())  # Expected output: "Queue is empty. Unable to dequeue data." 