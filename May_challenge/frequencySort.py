from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        val = []
        str_len = len(Counter(s))
        for i in Counter(s).most_common(str_len):
            val.append(i[0] * i[1])
        return "".join(val)


g = Solution().frequencySort("tree")
print(g)