class Solution:
    def subsetsWithDup(self, nums):

        # 1. sort the array
        # 2. if you get repeated number ignore it and move to next number
        # 3. perform backtracking - TC - (n*2^n)

        nums.sort()
        out = []

        def backtracking(start, end, res):
            out.append(res[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                res.append(nums[i])
                backtracking(i + 1, end, res)
                res.pop()

        backtracking(0, len(nums), res=[])
        return out


out = Solution().subsetsWithDup([1, 2, 2])
print(out)
