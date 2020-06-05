class Solution:
    def addDigits(self, num: int) -> int:

        while num > 10:
            sum = 0
            temp = num
            while temp !=0:
                sum += temp % 10
                temp //= 10
            num = sum
        return num





g = Solution()
out = g.addDigits(38)
print(out)