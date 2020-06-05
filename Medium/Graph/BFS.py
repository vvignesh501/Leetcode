import collections

class BreadthFirstSearch:

    def __init__(self):
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, v):
        visited = [False] * (max(self.graph)+1)
        queue = []
        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


g = BreadthFirstSearch()
g.addEdge(0, 1)  # Previous node, current node
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)