class Solution:
    def meetingRooms(self, intervals):
        intervals.sort()
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                return False
            else:
                prevEnd = end
        return True


out = Solution().meetingRooms([(0, 15), (15, 20)])
print(out)
