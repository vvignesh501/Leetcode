class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]

        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-2]):
            print(strs[0])
            print(strs[-2])
            if x == y:
                p += x
            else:
                break
        return p


val = ["abab", "ab"]
output = Solution().longestCommonPrefix(val)
print(output)


