# This is an input class. Do not edit.
import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.

    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True

    if tree.value < minValue or tree.value >= maxValue:
        return False

    left = validateBstHelper(tree.left, minValue, tree.value)
    right = validateBstHelper(tree.right, tree.value, maxValue)
    return left and right


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        out = validateBst(root)
        print(out)



