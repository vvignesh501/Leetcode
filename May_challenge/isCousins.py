class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        d = {}
        self.dfs(root, d, 0, None)

        if d[x][0] == d[y][0] and d[x][1] != d[y][1]:
            return True
        return False

    def dfs(self, root, dic, index, parent):

        if root is None:
            return None

        dic[root.val] = [index, parent]

        self.dfs(root.left, dic, index + 1, root)
        self.dfs(root.right, dic, index + 1, root)