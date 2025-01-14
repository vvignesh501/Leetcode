import collections


class Solution:
    def minDeletions(self, s: str) -> int:

        hash = {}
        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        res = 0
        used = set()

        for char, cnt in hash.items():
            while cnt > 0 and cnt in used:
                cnt -= 1
                res += 1
            used.add(cnt)
        return res


out = Solution().minDeletions("bbcebab")
print(out)
