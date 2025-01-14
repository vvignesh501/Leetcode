class Solution:
    def subsets(self, array):
        # Write your code here.
        # backtrack function
        out = []

        def backtracking(start, end, res):
            out.append(res[:])
            for i in range(start, end):
                res.append(array[i])  # left tree
                backtracking(i + 1, end, res)  # backtracking can be done only in the front, so i + 1
                res.pop()

        backtracking(0, len(array), res=[])
        return out


out = Solution().subsets([1, 2, 3])
print(out)
