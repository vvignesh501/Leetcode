class Solution(object):
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
        k = m + n - 1

        # Trick here is to remember that nums1 have a total of k length instead of m mentioned in the question.
        # Which ever is highest value from traversing reverse should be under nums1 filled from reverse.

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1


sol = Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
print(sol)
