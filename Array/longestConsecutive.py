class Solution:
    def longestConsecutive(self, nums):

        hashMap = dict()
        maxLength = 0

        for idx, num in enumerate(nums):
            hashMap[num] = idx

        for i in hashMap:

            # Create hashMap for all elements in nums.
            # If i - 1 not in hashMap that's the first element of the sequence
            # Eg: If 1 is in hashMap look for 2, 3, 4 etc.
            if (i - 1) not in hashMap:
                length = 1

                # If first sequence i.e 1 then check for 2,3,4 are in numSet
                while (i + length) in hashMap:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength


sol = Solution().longestConsecutive(nums=[100,4,200,1,3,2])
print(sol)