class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        for idx, character in enumerate(s):
            if not stack:
                stack.append(character)
            elif character in stack:
                continue
            else:
                while stack and (character < stack[-1]):
                    if stack[-1] in s[idx + 1:]:
                        _ = stack.pop()
                    else:
                        break

                stack.append(character)

        return ''.join(stack)


out = Solution().removeDuplicateLetters("cbacdcbc")
print(out)