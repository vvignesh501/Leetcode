class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ''
        res = 0
        if not s:
            return 0
        for ch in s:
            if ch not in longest_substring:
                longest_substring += ch
                if len(longest_substring) > res:
                    res += 1
            elif ch in longest_substring:
                index = longest_substring.find(ch)
                longest_substring = longest_substring[index + 1:] + ch
        return res


out = Solution().lengthOfLongestSubstring("pwwkew")
print(out)