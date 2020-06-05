class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        res = [0] * (N + 1)
        p = []
        for i, n in trust:
            res[n] += 1
            p.append(i)
        m = max(res)
        if m == N - 1 and res.index(m) not in p:
            return res.index(m)
        else:
            return -1


g = Solution()
out = g.findJudge(2, [[1, 2]])
print(out)
