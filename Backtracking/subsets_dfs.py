class Solution:
    def subsets(self, array):
        # Write your code here.
        # backtrack function
        res = []
        out = []

        def dfs(i):
            # constraint
            if i >= len(array):
                out.append(res[:])
                return

            res.append(array[i])
            dfs(i + 1)

            res.pop()
            dfs(i + 1)

        dfs(0)
        return out


out = Solution().subsets([1, 2, 3])
print(out)
