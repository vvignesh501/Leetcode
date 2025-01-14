class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        result, cur = 0, float("inf")
        last = ""
        nums.sort()
        for i in range(len(nums)):
            if not nums[i] == last:
                last = nums[i]
                j, k = i + 1, len(nums) - 1
                while j < k:
                    temp = nums[i] + nums[j] + nums[k]
                    if temp == target:
                        return temp
                    elif temp > target:
                        k -= 1
                    else:
                        j += 1
                    if abs(target - temp) < cur:
                        result = temp
                        cur = abs(target - temp)
        return result


out = Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1)
print(out)
