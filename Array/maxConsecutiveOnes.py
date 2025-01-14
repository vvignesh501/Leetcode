class Solution:
    def longestOnes(self, nums, k):
        left = right = 0
        for right in range(len(nums)):
            print(f"left={left}, right={right}, k={k}")
            print(nums[left:right + 1])
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1


if __name__ == "__main__":
    test = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]

    s = Solution()
    print(s.longestOnes(test, 2))
