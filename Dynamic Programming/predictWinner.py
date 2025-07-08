class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)
        arr = [0] * n
        
        for i in range(n-1,-1,-1):
            arr[i] = nums[i]
            
            for j in range(i+1, n):
                arr[j] = max(nums[i]-arr[j],
                             nums[j]-arr[j-1])
            
        return arr[n-1] >= 0

sol = Solution(nums = [1,5,2])
print(sol)
