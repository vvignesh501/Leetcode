from collections import deque


class Solution:
    def maze(self, maze, start, destination):

        m, n = len(maze), len(maze[0])
        q = deque([start])
        rs, cs = start
        vis = {(rs, cs)}
        while q:
            i, j = q.popleft()
            for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x, y = i, j
                while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] == 0:
                    x, y = x + a, y + b
                if [x, y] == destination:
                    return True
                if (x, y) not in vis:
                    vis.add((x, y))
                    q.append((x, y))
        return False


matrix = [[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]]
start, end = (0, 4), (3, 2)

out = Solution().maze(matrix, start, end)
print(out)