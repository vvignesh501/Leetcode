# Definition for a binary tree node.

# Time complexity - O(n) Space complexity - O(n)
# Since it goes through each node only once


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
    def levelOrderBottom(self, root: TreeNode):

        # Using DFS approach
        res = []

        def dfs(root, level):

            if not root:
                return None

            if level == len(res):
                res.append([])

            res[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return res[::-1]

    # def levelOrderBottom(self, root: TreeNode):
    # Using BFS
    #    q = deque()
    #    q.append(root)
    #    out = []
    #   while q:
    #      res = []
    #     qlen = len(q)
    #    for i in range(qlen):
    #       node = q.popleft()
    #      if node:
    #         res.append(node.val)
    #        q.append(node.left)
    #       q.append(node.right)
    # if res:
    #   out.append(res)
    # return out[::-1]


root = TreeNode(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
out = Solution().levelOrderBottom(root)
print(out)
