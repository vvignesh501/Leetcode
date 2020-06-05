class Solution:
    def backspaceCompare(self, S, T):
        stack1 = []
        stack2 = []
        for i in S:
            if i != "#":
                stack1.append(i)
            else:
                if stack1 != [] and i == "#":
                    stack1.pop(-1)
                elif not stack1:
                    stack1 = []

        for j in T:
            if j != "#":
                stack2.append(j)
            else:
                if stack2 != [] and j == "#":
                    stack2.pop(-1)
                elif not stack1:
                    stack1 = []

        if stack1 == stack2:
            return True
        else:
            return False


g = Solution()
out = g.backspaceCompare("a#c", "b")
print(out)