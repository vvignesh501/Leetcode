# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        # Neetcode - https://www.youtube.com/watch?v=0K0uCMYq5ng
        def helper(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, len(nums) - 1)


sol = Solution().sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
