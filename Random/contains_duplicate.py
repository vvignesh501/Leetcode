class Solution():
    def contains_duplicate(self, val):

        lists = list(val)
        while len(lists) != 0:
            for i in lists:
                if lists.count(i) > 1:
                    output = "true"
                else:
                    output = "false"
            return output


lists = [0]
output = Solution().contains_duplicate(lists)
print(output)
