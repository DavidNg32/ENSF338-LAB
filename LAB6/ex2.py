import timeit
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.leftChild = self._insert(root.leftChild, key)
        elif key > root.data:
            root.rightChild = self._insert(root.rightChild, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self._search(root.leftChild, key)
        return self._search(root.rightChild, key)

def binarySearch(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measureBuildTree(elements):
    random.shuffle(elements)
    
    tree = binaryTree()
    timeInsert = timeit.timeit(lambda: [tree.insert(element) for element in elements], number=10)

    timeSearch = timeit.timeit(lambda: [tree.search(element) for element in elements], number=10)

    return timeInsert / 10, timeSearch / 10

def measureBS(elements):
    random.shuffle(elements)
    sorted_elements = sorted(elements)

    binarySearchTime = timeit.timeit(lambda: [binarySearch(sorted_elements, element) for element in elements], number=10)

    return binarySearchTime / 10

def main():
    vector = list(range(10000))

    treeInsertTime, treeSearchTime= measureBuildTree(vector)
    print(f"\nBinary Search Tree's average insertion time || {treeInsertTime:.3f} seconds")
    print(f"Binary Search Tree's average search time || {treeSearchTime:.3f} seconds")

    binarySearchTime = measureBS(vector)
    print(f"\nBinary Search Average Time || {binarySearchTime:.3f} seconds\n")

if __name__ == "__main__":
    main()

# Question 4:
# Based on the results of our measurements, the time it takes regarding
# the binary search tree method is faster than the binary search on an array.
# on the result of a well-balanced tree, the time to search turns out to
# to be more effcient with insertion and search in this method.
# As the time complexity is O(log n) in the BST, more n elements become
# faster unlike binary search where it takes longer and slower with a high count of elements.
# in binary search, when we have O(log n) for searching, and O(n) for insertion, it takes longer.
# more often than not, the BST's search time turns out faster than the binary search of an array.