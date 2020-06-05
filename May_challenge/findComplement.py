class Solution:
    def findComplement(self, num: int) -> int:
        list = []
        out = bin(num)[2:]
        for i in out:
            if i == "0":
                list.append("1")
            elif i == "1":
                list.append("0")
        list = ''.join(list)
        return int(list, 2)


g = Solution()
out = g.findComplement(5)
print(out)