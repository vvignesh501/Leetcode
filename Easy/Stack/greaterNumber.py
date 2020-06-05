class Solution:
    def nextGreaterElement(self, nums1, nums2):
        out = []
        for i in nums1:
            for j in nums2[nums2.index(i):]:
                if j > i:
                    out.append(j)
                    break
            else:
                out.append(-1)
        return out


out = Solution()
result = out.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
print(result)
