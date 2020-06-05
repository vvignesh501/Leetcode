class Solution():
    def strStr(self, val1, val2):

        if val1 and val2:
            global sol
            letter = val2[0]
            if letter in val1:
                sol = val1.index(letter)
            else:
                sol = -1
            return sol


haystack = "hello"
needle = "ll"

solution = Solution()
sol = solution.strStr(haystack, needle)
print("{}".format(sol))

