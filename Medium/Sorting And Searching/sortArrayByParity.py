class Solution:
    def sortArrayByParityII(self, A):

        temp = [0]*len(A)
        i = 0
        j = 1
        for x in A:
            if x % 2 == 0:
                temp[i] = x
                i+=2
            else:
                temp[j] = x
                j+=2

        return temp



g = Solution()
out = g.sortArrayByParityII([4,2,5,7])
print(out)