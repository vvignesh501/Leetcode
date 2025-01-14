class Solution:
    def findOrder(self, numCourses: int, prerequisites):

        # use hashMap for DFS and use visit node for identifying if there are any cycles in a graph
        # for each courses perform a dfs

        hashMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            hashMap[crs].append(pre)

        queue = []
        visitSet = set()

        def dfs(crs, queue):

            # base case 1
            if crs in visitSet:
                return None

            # base case 2
            if hashMap[crs] == []:
                queue.append(crs)
                return True

            visitSet.add(crs)
            for pre in hashMap[crs]:
                if not dfs(pre, queue):
                    return None

        for crs in range(numCourses):
            if not dfs(crs, queue):
                return None


Solution().findOrder(2, [[1, 0]])
