# This is an input class. Do not edit.
class BinaryTre:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeNode:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def heightBalancedBinaryTree(tree):
    # Write your code here.

    # Base case
    if tree is None:
        return TreeNode(True, 1)

    leftNode = heightBalancedBinaryTree(tree.left)
    rightNode = heightBalancedBinaryTree(tree.right)

    if abs(leftNode.height - rightNode.height) <= 1:
        maxHeight = max(leftNode.height, rightNode.height) + 1
        return TreeNode(True, maxHeight)
    else:
        return False
    return True


BinaryTree = BinaryTre


class TestProgram:
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        actual = heightBalancedBinaryTree(root)
        print(actual)
