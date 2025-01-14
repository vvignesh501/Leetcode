class Solution:
    def longestMountain(self, array) -> int:
        # initiate and store the peak
        peak = False
        valley = False
        i = 0
        res = 0

        if len(array) < 3:
            return 0

        while i < len(array) - 1:
            if array[i] < array[i + 1]:
                start = i

                # collect both the increasing and decreasing items to get the peak
                # collect all the increasing items
                while i < len(array) - 1 and array[i] < array[i + 1]:
                    peak = True
                    i += 1

                # collect all the decreasing items
                while i < len(array) - 1 and array[i] > array[i + 1]:
                    valley = True
                    i += 1

                if peak == True and valley == True:
                    res = max(res, i - start + 1)
                peak = False
                valley = False
            else:
                i += 1
        return res


out = Solution().longestMountain([2, 1, 4, 7, 3, 2, 5])
print(out)
