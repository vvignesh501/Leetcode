class Solution:
    # def productExceptSelf(self, nums):
    #     res = [1] * (len(nums))
    #     prefix = 1
    #     for i in range(len(nums)):
    #         res[i] = prefix
    #         prefix *= nums[i]
    #     postfix = 1
    #     for j in range(len(nums)-1, -1, -1):
    #         res[j] *= postfix
    #         postfix *= nums[j]
    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create two arrays - postfix and prefix

        postfix = [1] * len(nums)
        prefix = [1] * len(nums)

        # Prefix and postfix contains values including the self
        # Remove the self

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        print(prefix, postfix)

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])

        return res         


out = Solution().productExceptSelf([1,2,3,4])
print(out)
