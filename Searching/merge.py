class Solution:
    def merge(self, nums1, m, nums2, n):
        print(sorted(nums1[:m] + nums2[:n]))
        for i, j in enumerate(sorted(nums1[:m] + nums2[:n])):
            nums1[i] = j
        return nums1

g = Solution()
out = g.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(out)


