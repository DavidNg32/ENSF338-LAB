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

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next