import unittest

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def _lr_rotate(self, node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _rl_rotate(self, node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            return self._lr_rotate(node)
        if balance < -1 and key < node.right.key:
            return self._rl_rotate(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_inorder(self, node):
        if node:
            self._print_inorder(node.left)
            print(node.key, end=" ")
            self._print_inorder(node.right)

    def print_inorder(self):
        self._print_inorder(self.root)
        print()


class TestAVLTree(unittest.TestCase):
    def test_case_3a(self):
        avl_tree = AVLTree()
        keys = [30, 20, 40, 10, 25, 35, 50, 5, 15, 28, 38, 48, 45]

        for key in keys:
            avl_tree.insert(key)

        expected_output = [5, 10, 15, 20, 25, 28, 30, 35, 38, 40, 45, 48, 50]
        result = self.traverse_inorder(avl_tree.root)
        self.assertEqual(result, expected_output)

    def test_case_3b_1(self):
        avl_tree = AVLTree()
        keys = [30, 20, 40, 10, 25, 35, 50, 5, 15, 28, 38, 48, 45, 42, 41]

        for key in keys:
            avl_tree.insert(key)

        expected_output = [5, 10, 15, 20, 25, 28, 30, 35, 38, 40, 41, 42, 45, 48, 50]
        result = self.traverse_inorder(avl_tree.root)
        self.assertEqual(result, expected_output)

    def test_case_3b_2(self):
        avl_tree = AVLTree()
        keys = [30, 20, 40, 10, 25, 35, 50, 5, 15, 28, 38, 48, 45, 42, 43]

        for key in keys:
            avl_tree.insert(key)

        expected_output = [5, 10, 15, 20, 25, 28, 30, 35, 38, 40, 42, 43, 45, 48, 50]
        result = self.traverse_inorder(avl_tree.root)
        self.assertEqual(result, expected_output)

    def traverse_inorder(self, node):
        result = []
        if node:
            result += self.traverse_inorder(node.left)
            result.append(node.key)
            result += self.traverse_inorder(node.right)
        return result

if __name__ == '__main__':
    unittest.main()