class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        ans = ""
        while columnNumber != 0:
            ans = s[(columnNumber + 25) % 26] + ans
            columnNumber = (columnNumber - 1) // 26

        return ans


out = Solution().convertToTitle(27)
print(out)