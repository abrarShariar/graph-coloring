class Graph:
    def __init__(self, totalNodes, adjacencyMatrix):
        self.totalNodes = totalNodes
        self.adjacencyMatrix = adjacencyMatrix
        self.color = [0]*totalNodes

    def isSafe(self, node, c):
        for i in range(len(self.adjacencyMatrix[node])):
            if(self.adjacencyMatrix[node][i] == 1 and self.color[i] == c):
                return False
        return True


    def graphColorUtil(self, node, colorLimit):
        if(node == self.totalNodes):
            return True

        for c in range(1, colorLimit+1):
            if(self.isSafe(node, c) == True):
                self.color[node] = c
                if(self.graphColorUtil(node+1, colorLimit) == True):
                    return True
                else:
                    self.color[node] = 0

        return False

    def graphColoring(self, startNode, colorLimit):
        self.color = [0]*self.totalNodes
        if(self.graphColorUtil(startNode, colorLimit) == True):
            return True
        else:
            print("Solution does not exists")
            return False


adjacencyMatrix = [
    [0,1,1,0,0,0],
    [1,0,1,1,0,0],
    [1,1,0,1,1,1],
    [0,1,1,0,1,0],
    [0,0,1,1,0,0],
    [0,0,1,0,0,0]
]
g = Graph(6, adjacencyMatrix)
colorLimit = 3
g.graphColoring(0, colorLimit)
print(g.color)
