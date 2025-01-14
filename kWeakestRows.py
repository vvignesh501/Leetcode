from heapq import heapify, heappush, heappop


class Solution:
    def kWeakestRows(self, mat, k: int):
        a = []
        for j, i in enumerate(mat):
            a.append([sum(i), j])
        a.sort()
        return [i[1] for i in a[:k]]

    def kWeakestRows(self, mat, k: int):
        heap = []
        heapify(heap)
        for j, i in enumerate(mat):
            x = i.count(1)
            heappush(heap, [x, j])

        return [heappop(heap)[1] for _ in range(k)]


out = Solution().kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3)
print(out)


