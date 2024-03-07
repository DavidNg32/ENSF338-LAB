import random
import timeit
class PriorityQueue1:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        self.queue = self.merge_sort(self.queue)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
        sorted_array = []
        while left_half and right_half:
            if left_half[0] < right_half[0]:
                sorted_array.append(left_half.pop(0))
            else:
                sorted_array.append(right_half.pop(0))
        sorted_array += left_half
        sorted_array += right_half
        return sorted_array

class PriorityQueue2:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if not self.queue:
            self.queue.append(item)
        else:
            for i, _item in enumerate(self.queue):
                if item < _item:
                    self.queue.insert(i, item)
                    return
            self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

def generate_tasks():
    tasks = []
    for _ in range(1000):
        task_type = 'enqueue' if random.random() < 0.7 else 'dequeue'
        tasks.append(task_type)
    return tasks

def measure_performance(queue_class):
    tasks = [generate_tasks() for _ in range(100)]
    start_time = timeit.default_timer()
    for task_list in tasks:
        queue = queue_class()
        for task in task_list:
            if task == 'enqueue':
                queue.enqueue(random.randint(1, 100))
            else:
                queue.dequeue()
    end_time = timeit.default_timer()
    print(f"Time taken by {queue_class.__name__}: {end_time - start_time}")

measure_performance(PriorityQueue1)
measure_performance(PriorityQueue2)

# The second implementation is faster than the first one. The first implementation uses merge sort to sort the queue 
# after every enqueue operation. The second implementation uses insertion sort to sort the queue after every enqueue 
# operation. The time complexity of merge sort is O(nlogn) and the time complexity of insertion sort is O(n^2). 
