class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:

        # Base case scenarios - Reject if it's any of these
        if arr[start] < 0 or start >= len(arr) or start < 0:
            return False

        # if reaches the destination return True
        if arr[start] == 0:
            return True

        print(start - arr[start], start + arr[start])
        # Recurse through the array and check if we can reach the destination 0

        if start - arr[start] >= 0:
            return self.canReach(arr, start - arr[start])

        if start + arr[start] <= len(arr):
            return self.canReach(arr, start + arr[start])


out = Solution().canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5)
print(out)
