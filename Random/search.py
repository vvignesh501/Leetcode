class Solution:
    def search(self, nums, target: int) -> int:

        if list:
            for x, y in enumerate(nums):
                if target in nums:
                    return x
                else:
                    return -1
            else:
                return -1
        else:
            return -1

g = Solution()
out = g.search([4,5,6,7,0,1,2], 0)
print(out)