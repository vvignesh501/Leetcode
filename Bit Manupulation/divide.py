class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        dividendd = abs(dividend)
        divisorr = abs(divisor)
        output = 0

        while dividendd >= divisorr:
            temp = divisorr
            mul = 1
            while dividendd >= temp:
                dividendd -= temp
                output += mul
                mul += mul
                temp += temp

        if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
            output = -output

        return min(2147483647, max(-2147483648, output))


out = Solution().divide(7, -3)
print(out)
