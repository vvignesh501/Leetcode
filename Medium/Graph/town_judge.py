import collections

class findTownJudge:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def addEdge(self, u , v):
        self.graph[u].append(v)

    def findJudge(self, v):
        visited = [False] * (max(self.graph)+1)
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                visited = True
            elif visited[i]:
                print(i)




g = findTownJudge()
g.addEdge(0,1)
g.addEdge(1,2)

g.findJudge(1)