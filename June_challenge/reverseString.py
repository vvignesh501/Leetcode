class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s


g = Solution().reverseString(["h", "e", "l", "l", "o"])
print(g)
