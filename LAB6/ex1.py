import timeit
import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(key)
                    return
            elif key > current.key:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(key)
                    return
            else:
                # Key already exists, do nothing
                return

    def search(self, key):
        current = self.root
        while current:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

# Generating a sorted vector
sorted_vector = list(range(10000))

# Building a tree by inserting each element
bst = BinarySearchTree()
for num in sorted_vector:
    bst.insert(num)

# Measuring search performance

def measure_search_performance():
    total_time = 0
    for num in sorted_vector:
        avg_time = timeit.timeit(lambda: bst.search(num), number=10)
        total_time += avg_time
    return total_time / len(sorted_vector), total_time

avg_time, total_time = measure_search_performance()
print("Search performance:")
print("Average time per search:", avg_time)
print("Total time for all searches:", total_time)
