import random
import matplotlib.pyplot as plt
import time

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insertRec(self.root, key)

    def insertRec(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self.insertRec(root.left, key)
        else:
            root.right = self.insertRec(root.right, key)
        return root

    def search(self, key):
        return self.searchRec(self.root, key)

    def searchRec(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.searchRec(root.left, key)
        return self.searchRec(root.right, key)

    def balanceMeasure(self):
        return self.measureBalRec(self.root)

    def measureBalRec(self, root):
        if root is None:
            return 0
        return max(self.measureBalRec(root.left), self.measureBalRec(root.right)) + 1

def checkPerform(bst, tasks):
    timeSearch = []
    balanceVal = []
    for task in tasks:
        start_time = time.time()  # Start timing
        search_time = 0
        for integer in task:
            node = bst.search(integer)
            search_time += 1
        end_time = time.time()  # End timing
        balance = bst.balanceMeasure()
        timeSearch.append(end_time - start_time)  
        balanceVal.append(balance)
    return timeSearch, balanceVal

def makeTasks():
    integers = list(range(1, 1001))
    random.shuffle(integers)
    return integers

def average(lst):
    return sum(lst) / len(lst)

if __name__ == "__main__":
    bst = BinarySearchTree()
    tasks = [makeTasks() for _ in range(1000)]
    avg_performance = []
    largest_balance = []
    for task in tasks:
        for integer in task:
            bst.insert(integer)
        timeSearch, balanceVal = checkPerform(bst, [task])
        avg_performance.append(average(timeSearch))
        largest_balance.append(max(balanceVal))
        bst.root = None  
    plt.scatter(largest_balance, avg_performance, alpha=0.5)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Average Search Time')
    plt.title('Balance vs. Search Time')
    plt.show()
