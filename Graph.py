#Graph
        
    #     2 -- 0
    #   /   \
    #  1 --- 3

class Graph():
    def __init__(self):
        self.numNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numNodes += 1
        return

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return


    def showConnections(self):
        print(self.adjacentList)
        return


graph = Graph()

graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)

graph.addEdge(3, 1)
graph.addEdge(3, 4)
graph.addEdge(4, 2)
graph.addEdge(4, 5)
graph.addEdge(1, 2)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(6, 5)

graph.showConnections()



