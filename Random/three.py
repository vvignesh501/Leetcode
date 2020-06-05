def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print([x for x in nums if nums.count(x) == 1])


if __name__ == '__main__':
    nums = [2, 2, 1]
    singleNumber(nums)
