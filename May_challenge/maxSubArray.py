from cmath import inf
from itertools import accumulate
class Solution:
  def maxSubarraySumCircular(self, A) -> int:
    a = max(accumulate(A, lambda s,x: max(x,s+x)))
    b = min(accumulate(A, lambda s,x: min(x,s+x)))
    return max(a, (sum(A)-b) or -inf)


g = Solution().maxSubarraySumCircular([1,-2,3,-2])
print(g)