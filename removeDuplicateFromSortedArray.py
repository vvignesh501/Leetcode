class Solution:
    def removeDuplicates(self, nums) -> int:
        i=j=0
        while j<len(nums):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1


if __name__ == '__main__':
    r = Solution()
    out = r.removeDuplicates([1, 1, 2])
    print(out)
