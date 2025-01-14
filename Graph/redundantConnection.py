class Solution:
    def findRedundantConnection(self, edges):

        n = len(edges)
        res = []
        parent = [i for i in range(n + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            x = edges[i][0]
            y = edges[i][1]

            find_x, find_y = find(x), find(y)
            if find_x != find_y:
                parent[find_y] = find_x
            else:
                res = x, y

        return res


out = Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])
print(out)