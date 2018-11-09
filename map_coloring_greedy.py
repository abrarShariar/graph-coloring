from collections import defaultdict

class Graph:
    def __init__(self, totalVertices):
        self.totalVertices = totalVertices
        self.adjacencyList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)
        self.adjacencyList[v].append(u)

    def graphColor(self, startNode):
        #initialize result array with -1
        result = [-1 for i in range(self.totalVertices)]
        #assign first color to startnode
        result[startNode] = 0
        #assign false for all color used list
        colorUsed = [False for i in range(self.totalVertices)]
        # assign color to remaining nodes
        for i in range(self.totalVertices):
            node = i+1
            if(node >= self.totalVertices):
                break

            for j in range(len(self.adjacencyList[node])):
                if(result[j] != -1):
                    colorUsed[result[j]] = True

            for k in range(len(colorUsed)):
                if(colorUsed[k] == False):
                    result[node] = k
                    break

            for a in range(len(self.adjacencyList[node])):
                if(result[a] != -1):
                    colorUsed[result[a]] = False

        return result

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(3, 4)

print(g.graphColor(0))
