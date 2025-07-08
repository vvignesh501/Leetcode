from functools import lru_cache

class Solution:    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def backtracking(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            # Try adding and subtracting the current number
            return backtracking(i + 1, total + nums[i]) + backtracking(i + 1, total - nums[i])
        
        return backtracking(0, 0) 

sol = Solution(nums = [18,47,49,45,31,13,45,44,33,45,44,43,21,30,23,46,43,10,3,30])
return sol
