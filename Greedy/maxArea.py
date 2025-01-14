class Solution:
    def maxArea(self, height: list[int]) -> int:

        area = 0
        l = 0
        r = len(height) - 1

        while l <= r:

            h = min(height[l], height[r])
            w = abs(r - l)
            area = max(area, h * w)

            if height[l] <= height[r]:
                l += 1

            if height[r] < height[l]:
                r -= 1

        return area


out = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(out)
