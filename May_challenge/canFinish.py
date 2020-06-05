class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        seen = set()
        while prerequisites:
            a, b = prerequisites.pop()
            if [b, a] in prerequisites:
                return False
            for x, y in prerequisites:
                if x == b:
                    if (y, a) in prerequisites:
                        return False
                    else:
                        if (a, b) not in seen:
                            prerequisites.append([a, y])
                            seen.add((a, b))
        return True


g = Solution().canFinish(2, [[1,0], [2,1]])
print(g)