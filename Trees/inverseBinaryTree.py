# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return

        leftNode = self.invertTree(root.left)
        rightNode = self.invertTree(root.right)

        root.left, root.right = rightNode, leftNode

        return root


a = TreeNode(4)
a.left = TreeNode(2)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)
a.right.left = TreeNode(6)
a.right.right = TreeNode(9)
out = Solution().invertTree(a)
print(out)

