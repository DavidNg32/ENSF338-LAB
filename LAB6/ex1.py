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

def createTree(sortmyVector):
    tree = BinarySearchTree()
    for i in sortmyVector:
        tree.insert(i)
    return tree

def measurePerf(tree, elements):
    overallTime = 0
    for i in elements:
        average = timeit.timeit(lambda: tree.search(i), number=10)
        overallTime += average
    return overallTime / len(elements), overallTime


def main():
    testVector = list(range(10000))

    treeSorted = createTree(testVector)
    average, overallTime = measurePerf(treeSorted, testVector)
    print(f"\nTime performance with a sorted vector || Average= {average} || Total= {overallTime}")

    random.shuffle(testVector)
    treeShuffle = createTree(testVector)
    average, overallTime = measurePerf(treeShuffle, testVector)
    print(f"\nTime performance with a shuffled vector || Average= {average} || Total= {overallTime}\n")

# Question 4:
# Based on the results of our measured performance regarding sorted vs
# shuffled, It is way more quicker to use the shuffled vector input.
# A unbalanced binary search tree runs less efficient than a balanced one.
# As larger trees call for longer search times this is due to imbalance in elements
# from a inserted vector that was sorted. In a case of shuffled insertion, it results
# in a vector that gives balance due to proper reaarangement.

if __name__ == "__main__":
    main()