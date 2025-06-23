class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = len(s.split()[-1])
        return last_word

ans = Solution().lengthOfLastWord(s="sdsfsf sdsdfs")
print(ans)
