from collections import Counter
class Solution:
    def majorityElement(self, nums):
        return Counter(nums).most_common()[0][0]

g = Solution()
out = g.majorityElement([2,2,1,1,1,2,2])
print(out)