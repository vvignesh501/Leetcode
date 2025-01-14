class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        res = 0
        intervals.sort()

        prev = intervals[0][1]  # First element in the first list [[1, 2]] - 1 is the first ele

        for start, end in intervals[1:]:
            # Check Previous first element and next first element
            if prev <= start:
                prev = end
            else:
                res += 1
                prev = min(prev, end)
        return res


out = Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
print(out)
