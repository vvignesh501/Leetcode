class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Choose 2 paths - left sum(candidates) right (pop the candidates)
        ans = []
        res = []
        def dfs(start, end, res, target):

            if sum(res) > target:
                return None

            if sum(res) == target:
                ans.append(res.copy())


            for i in range(start, end):
                res.append(candidates[i]) # left
                dfs(i, end, res, target) # backtrack
                res.pop() # right

        
        dfs(0, len(candidates), res, target)
        return ans

sol = Solution().combinationSum(candidates = [2,3,6,7], target = 7)

        
