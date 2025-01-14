# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        # TC1 - If subRoot is null, subTree inside root is a subTree itself. Return true
        if not subRoot:
            return True

        # TC2 - If root is null, subTree don't exist. Return false
        if not root:
            return False

        # If not TC1 and TC2
        if self.isSameTree(root, subRoot):
            return True

        # If left subTree or rightSubTree exist return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Checks if both the trees are same
    def isSameTree(self, p, q) -> bool:
        if p is not None and q is not None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        elif p is None and q is None:
            return True
        else:
            return False
