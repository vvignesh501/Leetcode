class Solution():
    def plusOne(self, val):
        output = ""
        for i in val:
            output = output + str(i)
        output = list(str(int(output) + 1))
        return list(map(int, output))

val = [5,2,2,1]
output = Solution().plusOne(val)
print(output)