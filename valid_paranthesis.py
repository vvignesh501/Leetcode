class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            else:
                # Append all the opening brackets to stack and when close brackets received and they don't
                # match the last ele of stack then return False else pop the elem from stack.
                # If stack is empty after all the ele then return True.
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if brackets[opening_bracket] != ch:
                    return False
        return len(stack) == 0





out = Solution()
result = out.isValid("")
print(result)
