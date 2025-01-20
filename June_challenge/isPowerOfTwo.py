import math


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n != 0:
            val = n & (n - 1) == 0
            return n & (n - 1) == 0
        else:
            return False


g = Solution().isPowerOfTwo(6)
print(g)
