class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = []
        days_profit = []
        for i in range(0, len(prices)):
            if i == 0 and prices[i] == max(prices):
                profit = prices[i]
                return profit
            else:
                for j in range(prices[i+1], len(prices)):
                    sell = prices[j] - prices[i]
                    days_profit.append(sell)
                max_profit = max(days_profit)

            return max_profit



g = Solution()
vals = [1,2,3,4,5]
print(max(vals), vals[0])
out = g.maxProfit(vals)
print(out)
