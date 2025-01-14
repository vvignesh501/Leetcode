import collections


class Solution:
    def isValidSudoku(self, board) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                if (board[i][j] in square[(i // 3, j // 3)] or
                        board[i][j] in rows[i] or
                        board[i][j] in cols[j]):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    square[(i // 3, j // 3)].add(board[i][j])
        return True


out = Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                   , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                   , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                   , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                   , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                   , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                   , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                   , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                   , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
print(out)