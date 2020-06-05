class Solution():
    def threesum(self, val):
        val.sort()
        sol = set()
        for i in range(0, len(val)-2):
            vals = set()
            for j in range(i+1, len(val)):
                c = -val[i] - val[j]
                if val[j] not in vals:
                    vals.add(c)
                else:
                    sol.add((val[i], val[j], c))
        return list(map(list, sol))


val = [-1,0,1,2,-1,-4]
output = Solution().threesum(val)
print(output)

