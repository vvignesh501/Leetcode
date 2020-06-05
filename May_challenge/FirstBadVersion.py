class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low <= high:
            mid = (low + high) >> 1
            if isBadVersion(mid):
                high = mid-1
            else:
                low = mid + 1
        return low



g = Solution()
out = g.firstBadVersion(5, 4)
print(out)
