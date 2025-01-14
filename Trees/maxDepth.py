# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        leftValue = self.maxDepth(root.left)
        rightValue = self.maxDepth(root.right)
        return 1 + max(leftValue, rightValue)

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(9)
out = Solution().maxDepth(a)
print(out)