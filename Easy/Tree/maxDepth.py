# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def calculate(self, root, m):
        if root == None:
            return 0
        return max([m, self.calculate(root.left, m + 1), self.calculate(root.right, m + 1)])

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.calculate(root, 1)

g = Solution()
out = g.maxDepth([3,9,20,0,0,15,7])
print(out)