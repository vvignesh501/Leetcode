"""
Using Brute force approach
"""


class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                diff = prices[j] - prices[i]
                profit = max(diff, profit)
        return profit


out = Solution().maxProfit([7, 6, 4, 3, 1])
print(out)
