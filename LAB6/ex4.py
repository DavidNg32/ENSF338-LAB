import random
import unittest

#Question 1
class heap1:
    def __init__(self):
        self.heap = []

    def heapify(self, array):
        self.heap = array
        for i in range(len(array) // 2 - 1, -1, -1):
            self.heapifydown(i)

    def enqueue(self, value):
        self.heap.append(value)
        self.heapifyup(len(self.heap) - 1)

    def dequeue(self):
        if self.heap == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifydown(0)

        return root

    def heapifyup(self, index):
        parentindex = (index - 1) // 2
        if index > 0 & self.heap[index] > self.heap[parentindex]:
            self.heap[index], self.heap[parentindex] = self.heap[parentindex], self.heap[index]
            self.heapifyup(parentindex)

    def heapifydown(self, index):
        n = len(self.heap)
        while True:
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            for child in (left_child, right_child):
                if child < n and self.heap[left_child] > self.heap[smallest]:
                    smallest = child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

#Question 2
class TestHeap1:
    def testheapsorted(self):
        expectedarray = [0,1,2,3,4,5,6,7,8,9]
        exheap = heap1()
        exheap.heapify(expectedarray)
        self.assertEqual(exheap.heap, expectedarray)
    def testheapempty(self):
        emparray = []
        exheap = heap1()
        exheap.heapify(emparray)
        self.assertEqual(exheap.heap, emparray)
    def testheaprandom(self):
        inputarray = [random.randint(100) for _ in range(100)]
        expectedarray = sorted(inputarray)
        exheap = heap1()
        exheap.heapify(inputarray)
        self.assertEqual(exheap.heap, expectedarray)

if __name__ == '__main__':
    unittest.main()