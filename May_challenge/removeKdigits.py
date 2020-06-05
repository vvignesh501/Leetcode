class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        while k > 0:
            length, i = len(num), 0
            while i + 1 < length and num[i] <= num[i + 1]:
                i += 1
            num = num[:i] + num[i + 1:]
            k -= 1
        num = num.lstrip('0')
        return num if num != "" else "0"


g = Solution()
out = g.removeKdigits("1432219", 3)
