from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Graph:
    def __init__(self, totalNodes, adjacencyList, color):
        self.totalNodes = totalNodes
        self.adjacencyList = adjacencyList
        self.color = color
        self.nodeSequence = [""]*totalNodes

    def isSafe(self,node, c):
        v = self.nodeSequence[node]
        for i in range(len(self.adjacencyList[v])):
            if(self.color[self.adjacencyList[v][i]] == c):
                return False
        return True


    def graphColorUtil(self, node, colorLimit):
        if node == self.totalNodes:
            return True

        for c in range(1, colorLimit+1):
            if(self.isSafe(node, c) == True):
                self.color[self.nodeSequence[node]] = c
                if(self.graphColorUtil(node+1, colorLimit) == True):
                    return True
                else:
                    self.color[self.nodeSequence[node]] = 0

        return False


    def graphColoring(self, startNode, colorLimit, nodeSequence):
        self.nodeSequence = nodeSequence
        if(self.graphColorUtil(startNode, colorLimit) == True):
            return True
        else:
            print("Solution does not exists")
            return False


def main():
    adjacencyList = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q'],
        'V': ['SA'],
        'T': ['V']
    };

    color = {
        'WA': 0,
        'NT': 0,
        'SA': 0,
        'Q': 0,
        'NSW': 0,
        'V': 0,
        'T': 0
    };

    nodeSequence = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    g = Graph(7, adjacencyList, color)
    colorLimit = 3
    g.graphColoring(0, colorLimit, nodeSequence)

    for i in range(len(nodeSequence)):
        print(nodeSequence[i], Color(color[nodeSequence[i]]))

main()
