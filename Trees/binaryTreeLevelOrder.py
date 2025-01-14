# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data


class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        q = collections.deque([root])

        while q:
            level = []
            # For BST you have to find the len of root at each level and run only for those level.
            qLen = len(q)

            # Run the current depth by popping the current depth and append the next depth values.
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res


root = TreeNode(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
out = Solution().levelOrder(root)
print(out)
