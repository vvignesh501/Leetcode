# A binary tree node
class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        # if the current node value is the same as p or q
        if root.value == p or root.value == q:
            return root

        print(root.value)
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if not right_res:
            return left_res
        if not left_res:
            return right_res

        return root


# Let us create a binary tree given in the above example
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
out = Solution().lowestCommonAncestor(root, 1, 8)
print(out.value)

