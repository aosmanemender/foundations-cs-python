class AdjacencyMatrix:  # undirected, weighted graph

  def __init__(self, V):
    self.matrix = []
    for _i in range(V):
      self.matrix.append([0] * V)

  def addEdge(self, vs, ve, weight): #O(1)
    self.matrix[vs][ve] = weight
    self.matrix[ve][vs] = weight  # makes the graph undirected

  def deleteEdge(self, vs, ve): #O(1)
    self.matrix[vs][ve] = 0
    self.matrix[ve][vs] = 0

  def showGraph(self): #O(v), v number of vertices
    for i in self.matrix:
      print(i)

  def areConnected(self, vs, ve, weight): #O(1)
    connected = self.matrix[vs][ve] == weight
    print(f"\n-> {vs} and {ve} are{'' if connected else ' not'} connected") 

  def citiesDirectlyReachable(self, vs, weight): #O(v), v number of vertices
    print(f"\n-> Cities directly reachable from {vs} are: ", end="")
    for i in range(len(self.matrix)):
      if self.matrix[vs][i] == weight:
        print(i, end=" ")

def Main5():
  G=AdjacencyMatrix(5)
  G.addEdge(0,1,1)
  G.addEdge(1,2,1)
  G.addEdge(1,3,1)
  G.addEdge(2,3,1)
  G.showGraph()
  G.areConnected(0, 3, 1)
  G.citiesDirectlyReachable(3, 1)
  print("\n")

Main5()