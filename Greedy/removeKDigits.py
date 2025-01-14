class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for i in num:
            while stack and i < stack[-1] and k:
                _ = stack.pop()
                k -= 1

            if not stack and i == "0":
                continue

            stack.append(i)

        return "0" if not stack or k >= len(stack) else "".join(stack[:len(stack) - k])


out = Solution().removeKdigits("987654321", 3)
print(out)
