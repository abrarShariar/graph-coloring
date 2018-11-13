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

    def isSafe(self, node, c):
        for i in range(len(self.adjacencyList[node])):
            if(self.color[self.adjacencyList[node][i]] == c):
                return False
        return True


    def graphColorUtil(self, node, colorLimit):
        if node == '':
            return True

        for c in range(1, colorLimit+1):
            if(self.isSafe(node, c) == True):
                self.color[node] = c
                nextNode = self.pickNode(node)
                if(self.graphColorUtil(nextNode, colorLimit) == True):
                    return True
                else:
                    self.color[node] = 0

        return False



    def graphColoring(self, colorLimit):
        startNode = self.pickNode('')
        if(self.graphColorUtil(startNode, colorLimit) == True):
            return True
        else:
            print("Solution does not exists")
            return False


    # pick node using MRV
    def pickNode(self, initialNode):
        maxCount = 0
        selectedNode = ''
        # the very first node
        if (initialNode == ''):
            for node, neighbourList in self.adjacencyList.iteritems():
                if (len(neighbourList) > maxCount and self.color[node] == 0):
                    maxCount = len(neighbourList)
                    selectedNode = node
        # the other nodes
        else:
            for i in range(len(self.adjacencyList[initialNode])):
                childNode = self.adjacencyList[initialNode][i]
                if (self.color[childNode] == 0 and len(self.adjacencyList[childNode]) > maxCount):
                    maxCount = len(self.adjacencyList[childNode])
                    selectedNode = childNode

        return selectedNode

def main():
    adjacencyList = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q'],
        'V': ['SA', 'T'],
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

    # nodeSequence = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    g = Graph(7, adjacencyList, color)
    colorLimit = 3
    g.graphColoring(colorLimit)

    # for i in range(len(nodeSequence)):
    #     print(nodeSequence[i], Color(color[nodeSequence[i]]))

    for node, color in g.color.iteritems():
        print(node, (color))
main()
