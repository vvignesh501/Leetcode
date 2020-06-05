def containsDuplicate(nums):
    """
        :type nums: List[int]
        :rtype: bool
        """
    if any(nums.count(i) > 1 for i in nums):
        print("True")
        return True
    else:
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    containsDuplicate(nums)
