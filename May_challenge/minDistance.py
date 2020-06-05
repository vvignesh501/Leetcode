class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if len(word1) * len(word2) == 0:
            return len(word1) + len(word2)

        stack = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            stack[i][0] = i
        for i in range(len(word2) + 1):
            stack[0][i] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    stack[i][j] = stack[i - 1][j - 1]
                else:
                    stack[i][j] = 1 + min(stack[i - 1][j], min(stack[i][j - 1], stack[i - 1][j - 1]))
        return stack[len(word1)][len(word2)]


g = Solution().minDistance("horse", "ros")
print(g)
