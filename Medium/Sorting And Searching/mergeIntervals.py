from copy import deepcopy


class Solution:
    def merge(self, intervals):
        i = 1
        intervals.sort()
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1] = [intervals[i - 1][0], max(intervals[i][1], intervals[i - 1][1])]
                intervals.pop(i)
            else:
                i += 1
        return intervals


g = Solution()
copy = deepcopy(g)
out1 = copy.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
out2 = g.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(out1)
