# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    res = [0]

    def traverse(tree):
        # Height of the null tree
        if not tree:
            return -1

        left = traverse(tree.left)
        right = traverse(tree.right)

        # diameter = 2 edges (left and right) + left + right
        res[0] = max(res[0], 2 + left + right)
        # height = 1 (edge - either left or right) max of left (or) right height
        return 1 + max(left, right)

    traverse(tree)
    return res[0]


a = BinaryTree(5)
a.left = BinaryTree(3)
a.right = BinaryTree(9)
out = binaryTreeDiameter(a)
print(out)
