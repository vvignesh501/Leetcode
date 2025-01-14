class Solution:
    def containsDuplicate(self, nums) -> bool:
        new_list = list(dict.fromkeys(nums))
        if new_list != nums:
            return True
        elif new_list == nums:
            return False


out = Solution().containsDuplicate([1, 2, 3, 1])
print(out)
