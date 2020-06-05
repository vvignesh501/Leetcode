class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x1 = str(x)
        x1 = x1[::-1]
        x1 = [x1[1:] if x1[0] == '0' else x1]
        return x1[0]


val = 120
output = Solution().reverse(val)
print(output)
