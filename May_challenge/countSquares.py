class Solution:
    def countSquares(self, M) -> int:
        m = len(M)
        n = len(M[0])
        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if M[i - 1][j - 1] == 1:
                    matrix[i][j] = 1 + min([matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]])
                    count += matrix[i][j]
        return count


g = Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
print(g)