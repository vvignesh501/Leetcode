class Solution:
    def find132pattern(self, nums):
        temp, val = float('-inf'), []
        for i in nums[::-1]:
            if i < temp:
                return True
            while val and i > val[-1]:
                temp = val.pop()
            val.append(i)
        return False





g = Solution()
out = g.find132pattern([3, 1, 4, 2])
print(out)