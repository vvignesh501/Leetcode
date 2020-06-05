class Solution(object):
    def kClosest(self, points, K):
        val = []
        points = sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)
        for i in range(K):
            val.append(points[i])
        return val


g = Solution().kClosest([[1, 3], [-2, 2]], 1)
print(g)
