class Node:
    def __init__(self, name):
        self.name = name
        self.color = ''
        self.adjacencyList = []
     
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
                

class Graph:
    def __init__(self, nodeList):
        self.nodeList = nodeList
        
    def showAdjacencyList(self):
        for i in range(len(self.nodeList)):
            print("Node: ", self.nodeList[i].name)
            print("Adjacency List: ") 
            for node in self.nodeList[i].adjacencyList:
                print(node.name, " ")
        
        
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
    Q.addNeighbour(NT);
    Q.addNeighbour(SA);
    Q.addNeighbour(NSW);
    NSW.addNeighbour(SA);
    NSW.addNeighbour(Q);
    NSW.addNeighbour(V);
    V.addNeighbour(NSW);
    V.addNeighbour(SA);
    
    graph = Graph([WA, NT, SA, Q, NSW, V])
    
    travelSequence = [WA, NT, Q, NSW, V, SA]
    colorSequence = ['R', 'G', 'B']
    
    # graph.showAdjacencyList()

   
main()
