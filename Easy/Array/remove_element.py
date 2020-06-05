class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        nums[:] = [i for i in nums if i != val]
        return nums


g = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
out = g.removeElement(nums, val)
print(out, len(out))
