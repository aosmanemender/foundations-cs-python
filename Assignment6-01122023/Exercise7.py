
class AdjacencyMatrix3:  # undirected, weighted graph

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

  def showGraph(self): #O(n)
    for i in self.matrix:
      print(i)

  def displayCommonFollowing(self, u1, u2, weight): #O(n)
    print(f"\n-> Users followed by both {u1} and {u2}: ", end="")
    for i in range(len(self.matrix)):
      if self.matrix[u1][i] == weight and self.matrix[u2][i] == weight:
        print(i, end=" ")

  def displayNonFollowed(self, weight): #O(n)
    print("\n-> Users non followed by anyone: ", end="")
    for i in range(len(self.matrix)):
      if weight not in self.matrix[i]:
        print(i, end=" ")

def Main7():
  G=AdjacencyMatrix3(5)
  G.addEdge(0,2,1)
  G.addEdge(0,3,1)
  G.addEdge(1,2,1)
  G.addEdge(1,3,1)
  G.addEdge(2,3,1)
  G.showGraph()
  G.displayCommonFollowing(0, 1, 1)
  G.displayNonFollowed(1)
  print("\n")

Main7()