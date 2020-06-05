class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = []
        max_length = 0
        for i in s:
            if i in letters:
                letters = letters[letters.index(i) + 1:]
            letters.append(i)
            length = max(max_length, len(letters))
        return length


s = "abcabcabsa"
i = 0
long_string = Solution().lengthOfLongestSubstring(s)
print(long_string)