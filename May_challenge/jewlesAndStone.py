class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        num = 0
        for i in J:
            num += S.count(i)
        return num


g = Solution()
out = g.numJewelsInStones("aA", "aAAbbbb")
print(out)