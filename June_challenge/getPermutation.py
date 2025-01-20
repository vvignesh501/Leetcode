import itertools

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        plist = itertools.permutations([str(i) for i in range(1, n + 1)])
        for i in range(k - 1):
            plist.__next__()
        return ''.join(plist.__next__())


g = Solution().getPermutation(3, 3)
print(g)