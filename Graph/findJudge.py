class Solution:
    def findJudge(self, n: int, trust) -> int:
        no_of_people = [0] * (n + 1)
        for i in range(len(trust)):
            a = trust[i][0]
            b = trust[i][1]

            no_of_people[a] -= 1
            no_of_people[b] += 1

        for judge in range(1, n+1):
            if no_of_people[i] == n - 1:
                return judge
        return -1


out = Solution().findJudge(2, [[1, 2]])
print(out)
