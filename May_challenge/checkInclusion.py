import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count = collections.Counter(s1)
        string_len = len(s1)
        for i in range(0, len(s2)):
            while s2[i] not in set(s1) and i < len(s2):
                i += 1
                if i >= len(s2):
                    return False
            if collections.Counter(s2[i:i + string_len]) == count:
                return True


g = Solution().checkInclusion("ab", "eidbaooo")
print(g)
