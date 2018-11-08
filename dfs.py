from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge (self, f, to):
        self.graph[f].append(to)

    def DFSUtil (self, node, visited):
        print(node)
        if visited[node] == False:
            visited[node] = True

        for n in self.graph[node]:
            if (visited[n] == False):
                self.DFSUtil (n, visited)

    def DFS (self, startNode):
        visited = [False]*(len(self.graph))
        self.DFSUtil(startNode, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from - starting from vertex 2")
g.DFS(2)
