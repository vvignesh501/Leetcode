class Solution:
    def exist(self, board, word: str) -> bool:

        visited = set()

        def dfs(r, c, char):

            if char == len(word):
                return True

            # base case
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited or board[r][c] != word[
                char]:
                return False

            visited.add((r, c))
            res = (dfs(r + 1, c, char + 1) or
                   dfs(r - 1, c, char + 1) or
                   dfs(r, c + 1, char + 1) or
                   dfs(r, c - 1, char + 1))
            visited.remove((r, c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False


out = Solution().exist([["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]], "ABCCED")
print(out)
