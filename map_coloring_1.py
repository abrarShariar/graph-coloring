class Node:
    def __init__(self, name):
        self.name = name
        self.color = ''
        self.adjacencyList = []
        self.colorCodeUsed = []

    def addNeighbour(self, node):
        if isinstance(node, Node) and not self.neighbourExist(node):
            self.adjacencyList.append(node)

    def neighbourExist(self, node):
        for i in range(len(self.adjacencyList)):
            if len(self.adjacencyList) <= 0:
                return False
            elif (self.adjacencyList[i].name == node.name):
                return True
            else:
                return False

    def colorNode(self, colorList):
        colorCount = 0
        for i in range(len(colorList)):
            for j in range(len(self.adjacencyList)):
                child = self.adjacencyList[j]
                if(child.color == colorList[i]):
                    colorCount += 1

        if(colorCount >= len(self.adjacencyList)):
            return False
        else:
            if(len(self.colorCodeUsed) > len(colorList)):
                return False
            else:
                if(self.color == 'R'):
                    self.color = 'G'
                elif(self.color == 'G'):
                    self.color = 'B'
                elif(self.color == 'B'):
                    self.color = 'R'
                    self.colorCodeUsed.append(self.color)
                return True

class Graph:
    def __init__(self, nodeList):
        self.nodeList = nodeList
        self.travelSeq = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA']
        self.colorList = ['R', 'G', 'B']

    def showAdjacencyList(self):
        for i in range(len(self.nodeList)):
            print("Node: ", self.nodeList[i].name)
            print("Adjacency List: ")
            for node in self.nodeList[i].adjacencyList:
                print(node.name, " ")

    def findNextNode(self, node):
        index = 0
        for i in range(len(self.travelSeq)):
            if (self.travelSeq[i] == node.name):
                index = i + 1
                break

        for j in range(len(node.adjacencyList)):
            if (node.adjacencyList[j].name == self.travelSeq[index]):
                return node.adjacencyList[j]



    def color(self, node, visitStack):
        # check if color is safe then apply color on node
        if(len(visitStack) >= len(self.nodeList)):
            return

        if(node.colorNode(self.colorList)):
            print(node.name, node.color)
            visitStack.append(node)
            nextNode = self.findNextNode(node)
            self.color(nextNode, visitStack)
        else:
            if(len(visitStack) > 0):
                nextNode = visitStack.pop()
                self.color(nextNode, visitStack)

def main():

    WA = Node("WA")
    NT = Node("NT")
    SA = Node("SA")
    Q = Node("Q")
    NSW = Node("NSW")
    V = Node("V")

    WA.addNeighbour(NT)
    WA.addNeighbour(SA)
    NT.addNeighbour(SA)
    NT.addNeighbour(WA)
    NT.addNeighbour(Q)
    SA.addNeighbour(WA)
    SA.addNeighbour(NT)
    SA.addNeighbour(Q)
    SA.addNeighbour(NSW)
    SA.addNeighbour(V)
    Q.addNeighbour(NT)
    Q.addNeighbour(SA)
    Q.addNeighbour(NSW)
    NSW.addNeighbour(SA)
    NSW.addNeighbour(Q)
    NSW.addNeighbour(V)
    V.addNeighbour(NSW)
    V.addNeighbour(SA)

    graph = Graph([WA, NT, SA, Q, NSW, V])
    # graph.showAdjacencyList()

    visitStack = []

    graph.color(WA, visitStack)

    # print(visitStack)

    # print(WA.color)


main()
