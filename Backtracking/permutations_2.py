class Solution:
    def permuteUnique(self, nums):
        hashMap = {}

        for i in nums:
            if i in hashMap:
                hashMap[i] = hashMap[i] + 1
            else:
                hashMap[i] = 1

        def backtracking():

            if len(res) == len(nums):
                ans.append(res[:])
                return

            for i in hashMap:
                if i in hashMap and hashMap[i] > 0:
                    res.append(i)
                    hashMap[i] -= 1

                    backtracking()

                    hashMap[i] += 1
                    res.pop()

        ans = []
        res = []
        backtracking()
        return ans


out = Solution().permuteUnique([1, 2, 3])
print(out)
