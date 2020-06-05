class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=""
        dicts = {"(": ")", "{": "}", "[": "]"}
        for x, y in dicts.items():
            if s[0] == x and s[1] == y:
                a = "true"
        if a == "":
            a = "false"
        return a


string = "(]"
output = Solution().isValid(string)
print(output)
