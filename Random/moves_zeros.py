class Solution(object):
    def moveZeros(self, nums):
        s,f = 0,1
        while f < len(nums):
            if nums[f] == 0:
                f+=1
            else:
                # f non-zero
                if nums[s] == 0:
                    # f non-zero, s zero
                    nums[s], nums[f] = nums[f], nums[s]
                s+=1

            # make sure f faster than s
            if s==f:
                f+=1
            return

val = [0,1,0,3,12]
output = Solution().moveZeros(val)
print(output)