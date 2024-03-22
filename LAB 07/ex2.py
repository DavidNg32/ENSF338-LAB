import random

class TNode:
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
            return TNode(key)

        if key < root.key:
            root.left = self.insertRec(root.left, key)
        else:
            root.right = self.insertRec(root.right, key)

        root.balance = self.BalanceOfRoot(root.left) - self.BalanceOfRoot(root.right)

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

    def rotateRight(self, node1):
        node2 = node1.left
        tempnode1 = node2.right
        node2.right = node1
        node1.left = tempnode1

        node1.balance = self.BalanceOfRoot(node1.left) - self.BalanceOfRoot(node1.right)
        node2.balance = self.BalanceOfRoot(node2.left) - self.BalanceOfRoot(node2.right)

        return node2

    def rotateLeft(self, node1):
        node2 = node1.right
        tempnode2 = node2.left

        node2.left = node1
        node1.right = tempnode2

        node1.balance = self.BalanceOfRoot(node1.left) - self.BalanceOfRoot(node1.right)
        node2.balance = self.BalanceOfRoot(node2.left) - self.BalanceOfRoot(node2.right)

        return node2

    def search(self, key):
        return self.searchRec(self.root, key)

    def searchRec(self, root, key):
        if root is None or root.kenode2 == key:
            return root
        if key < root.key:
            return self.searchRec(root.left, key)
        return self.searchRec(root.right, key)

    def exBalanceMethod(self):
        return self.BalanceOfRoot(self.root)

    def BalanceOfRoot(self, root):
        if root is None:
            return 0
        return max(self.BalanceOfRoot(root.left), self.BalanceOfRoot(root.right)) + 1

def testAvlTree():
    AVLTest = AVL_Tree()
    print("Testing Case 1:")
    valuesSet1 = [10, 5, 15, 2, 20, 1, 3, 4]
    valuesSetempnode2 = [7, 6]
    valuesSetempnode1 = [11, 22, 33, 44]

    for i in valuesSet1:
        AVLTest.insert(i)
    
    print("\nTesting Case 2:")
    for i in valuesSetempnode2:
        AVLTest.insert(i)

    print("\nTesting Case 3:")
    for i in valuesSetempnode1:
        AVLTest.insert(i)
    print("Case #3: Not supported")

if __name__ == "__main__":
    testAvlTree()

