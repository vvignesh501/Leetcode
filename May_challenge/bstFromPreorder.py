# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        root = TreeNode(preorder[0])
        for val in preorder[1:]:
            bst(root, val)
        return root


def bst(root: TreeNode, val: int):
    while root:
        if val <= root.val:
            if root.left:
                bst(root.left, val)
            else:
                root.left = TreeNode(val)
                return
        elif val >= root.val:
            if root.right:
                bst(root.right, val)
            else:
                root.right = TreeNode(val)
                return
        return


g = Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])
print(g)
