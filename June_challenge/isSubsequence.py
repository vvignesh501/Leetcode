class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_sort = sorted(s)
        t_sort = sorted(t)

        val = [i for i, j in zip(s_sort, t_sort) if i == j]
        val1 = ''.join(val)

        if val1 == s:
            return True
        else:
            return False


g = Solution().isSubsequence("abc", "acb")
print(g)