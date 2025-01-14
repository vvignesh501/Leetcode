class Solution:
    def partitionLabels(self, s: str):

        # Create hashmap with val as last time the char has appeared in the string
        hashMap = {}
        for i, char in enumerate(s):
            hashMap[char] = i

        # loop through again. If all chars less than last time a has appreared. Then that's the end
        # Take two pointers, start and end
        start, end = 0, 0
        res = []
        for i, char in enumerate(s):
            start += 1

            # Compare end ptr with hashMap val of a.0 > 8, then end = 8.
            # Compare 8 with next char. hashMap val of b is 5. 5 < 8, so end is still 8 and so on.
            if hashMap[char] > end:
                end = hashMap[char]

            # When i == 8, append the res and make start pointer to 0.
            if i == end:
                res.append(start)
                start = 0
        return res


out = Solution().partitionLabels("ababcbacadefegdehijhklij")
print(out)