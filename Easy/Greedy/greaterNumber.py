class Solution:
    def nextGreaterElements(self, nums1, nums2):

        out = []
        for i in nums1:
            j = nums2.index(i)
            if nums2[j] == nums2[-1]:
                out.append(-1)
            else:
                if i < nums2[j+1]:
                    out.append(nums2[j+1])
                else:
                    out.append(-1)
        return out




g = Solution()
out = g.nextGreaterElements([4,1,2], [1,3,4,2])
print(out)