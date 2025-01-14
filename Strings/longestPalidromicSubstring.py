class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Go from each element and traverse through left and right of each element.
        # For odd, take one element and traverse through left and right.
        # For even, take two elements and traverse through left and right.
        res = ""
        for i in range(len(s)):
            odd = self.palindrome(s, i, i)
            even = self.palindrome(s, i, i + 1)
            res = max(res, odd, even, key=len)
        return res

    def palindrome(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if s[l] == s[r]:
                l -= 1
                r += 1

        return s[l + 1:r]


out = Solution().longestPalindrome("babad")
print(out)