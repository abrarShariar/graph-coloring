class Graph:
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.listOfNodes = [[] for i in range(numberOfVertices)]

    def addEdge(self, fm, to):
        self.listOfNodes[fm].append(to)
        self.listOfNodes[to].append(fm)

    def showAdjacencyList(self):
        for i in range(len(self.listOfNodes)):
            print(i, end="-> ")
            for j in range(len(self.listOfNodes[i])):
                if (j == len(self.listOfNodes[i]) - 1):
                    print(self.listOfNodes[i][j])
                else:
                    print(self.listOfNodes[i][j], end="-> ")

def main():
    T = input()
    for i in range(int(T)):
        V, E = input().split()
        g = Graph(int(V))
        for j in range(int(E)):
            fm, to = input().split()
            g.addEdge(int(fm), int(to))

    g.showAdjacencyList()

main()
