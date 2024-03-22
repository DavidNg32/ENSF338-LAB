import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

class AVL_Tree:
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

        root.balance = self.measureBalanceRec(root.left) - self.measureBalanceRec(root.right)

        if root.balance > 1 or root.balance < -1:
            self.balanceNode(root, key)

        return root

    def balanceNode(self, node, key):
        if node.balance > 1 and key < node.left.key:
            print("Case #1: Pivot not detected")
            return self.rotateRight(node)

        if node.balance < -1 and key > node.right.key:
            print("Case #1: Pivot not detected")
            return self.rotateLeft(node)

        if node.balance > 1 and key > node.left.key:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        if node.balance < -1 and key < node.right.key:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        print("Case #3: Not supported")

    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        z.balance = self.measureBalanceRec(z.left) - self.measureBalanceRec(z.right)
        y.balance = self.measureBalanceRec(y.left) - self.measureBalanceRec(y.right)

        return y

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.balance = self.measureBalanceRec(z.left) - self.measureBalanceRec(z.right)
        y.balance = self.measureBalanceRec(y.left) - self.measureBalanceRec(y.right)

        return y

    def search(self, key):
        return self.searchRec(self.root, key)

    def searchRec(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.searchRec(root.left, key)
        return self.searchRec(root.right, key)

    def measureBalance(self):
        return self.measureBalanceRec(self.root)

    def measureBalanceRec(self, root):
        if root is None:
            return 0
        return max(self.measureBalanceRec(root.left), self.measureBalanceRec(root.right)) + 1

def testAvlTree():
    AVLTest = AVL_Tree()
    print("Testing Case 1:")
    valuesSet1 = [10, 5, 15, 2, 20, 1, 3, 4]
    valuesSet2 = [7, 6]
    valuesSet3 = [11, 22, 33, 44]

    for i in valuesSet1:
        AVLTest.insert(i)
    
    print("\nTesting Case 2:")
    for i in valuesSet2:
        AVLTest.insert(i)

    print("\nTesting Case 3:")
    for i in valuesSet3:
        AVLTest.insert(i)
    print("Case #3: Not supported")

if __name__ == "__main__":
    testAvlTree()

