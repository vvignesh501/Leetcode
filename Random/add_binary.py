class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print (int(a,2))
        print(int(b,2))
        sum = bin(int(a,2) + int(b,2))
        print(sum)
        return sum[2:]


g = Solution()
out = g.addBinary("1100", "010")
print(out)