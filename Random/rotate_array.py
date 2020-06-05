class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        output = []
        sorted_nums = list(nums)
        # sorted_nums.sort(reverse=True)
        # print("Sorted:", sorted_nums)
        length = len(nums)
        output = nums[(length - k):] + nums[:(length - k)]
        return output


array = [-1, -100, 3, 99]
k = 2

output = Solution().rotate(array, k)
print(output)
