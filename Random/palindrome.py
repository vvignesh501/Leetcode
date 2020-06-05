class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            j = i + 1
            while j <= len(s) and len(res) <= len(s[i:]):
                print(len(s), len(res), len(s[i:]))
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    print(s[i:j], s[i:j][::-1], len(s[i:j]), len(res))
                    res = s[i:j]
                    print(res)
                j+=1
        return res


s = "babad"
palindrome = Solution().longestPalindrome(s)
print(palindrome)
