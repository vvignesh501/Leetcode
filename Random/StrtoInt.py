import re


class Solution():
    def stringToInt(self, val):
        output = val.split(' ')
        output = list(filter(None, output))
        if str(output[0]).isnumeric() or output[0][:1] in ("+", "-"):
            print(str(output[0][1:]), pow(2, 31))
            output = [-2147483648 if int(str(output[0][1:])) >= pow(2, 31) else output[0]]
        else:
            output = '0'

        return output


val = "+91283472332"
output = Solution().stringToInt(val)
print(str(output[0]))
