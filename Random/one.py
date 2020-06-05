def rotate(nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    n = len(nums)
    rotated_list = []
    sort_list = nums[-k:]
    sorted_list = nums[:n - k]
    rotated_list = sort_list + sorted_list
    print(rotated_list)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    rotate(nums, k)
