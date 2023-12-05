
class AdjacencyMatrix2:  # directed, weighted graph

  def __init__(self, V):
    self.matrix = []
    for _i in range(V):
      self.matrix.append([0] * V)

  def addEdge(self, vs, ve, weight): #O(1)
    self.matrix[vs][ve] = weight

  def deleteEdge(self, vs, ve): #O(1)
    self.matrix[vs][ve] = 0

  def showGraph(self): #O(v), v number of vertices
    for i in self.matrix:
      print(i)

  def areConnected(self, vs, ve, weight): #O(1)
    connected = self.matrix[vs][ve] == weight or self.matrix[ve][vs] == weight
    print(f"\n-> {vs} and {ve} are{'' if connected else ' not'} connected") 

  def citiesDirectlyReachableFrom(self, vs, weight): #O(v), v number of vertices
    # print(f"\n-> Cities directly reachable from {vs} are: ", end="")
    cities = []
    for i in range(len(self.matrix)):
      if self.matrix[vs][i] == weight:
        cities.append(i)

    # if cities:
    #   for i in cities:
    #     print(i, end=" ")
    # else:
    #   print("∅")

    return cities

  def graphContainsCycle(self, weight): #O(v^3), v number of vertices
    cities = []

    for i in range(len(self.matrix)):
      cities.append(self.citiesDirectlyReachableFrom(i, weight))

    # cities=  [[1], [2], [3], [4], [1]]
    print("\n\ncities= ", cities)
    for i in range(len(cities)): #O(v), v number of cities
      for k in range(len(cities)): #O(v)
        if i in cities[k]:
          cyclic = self.helper2(cities, i, k, []) #O(v)
          if cyclic:
            return

  def helper2(self, cities, i, k, alreadyScanned): #O(v)
    alreadyScanned.append(i)
    if k in cities[i]:
      for elt in alreadyScanned:
        print(elt, end = " -> ")
      print(f"{k} -> {alreadyScanned[0]} \tform a cycle")
      return True

    for j in cities[i]: #O(v)
      if j not in alreadyScanned:
        self.helper2(cities, j, k, alreadyScanned)

    return False

  def helper(self, cities, i, k, alreadyScanned):
    print("\nalreadyScanned= ", alreadyScanned)
    if i >= len(cities) or k >= len(cities):
      return False

    if k in cities[i]:
      # cycle
      print(f"{alreadyScanned[0]} and {k} form a cycle")
      return True

    alreadyScanned.append(i)
    print(f"i= {i}, cities[{k}]= {cities[k]}")
    for j in cities[i]:
      print(f"\tj= {j}, cities[{i}]= {cities[i]}")
      print(f"\t? k= {k} in cities[{j}]= {cities[j]}")
      if k in cities[j]:
        # cycle
        print(f"{i} and {k} form a cycle")
        return True
      else:
        alreadyScanned.append(j)
        print("-> alreadyScanned= ", alreadyScanned)
        for p in cities[j]:
          if p not in alreadyScanned:
            self.helper(cities, p, k, alreadyScanned)
            
def Main6():
  G=AdjacencyMatrix2(5)
  G.addEdge(0,1,1)
  G.addEdge(1,2,1)
  # G.addEdge(3, 1, 1)
  G.addEdge(2,3,1)
  G.addEdge(3,4,1)
  G.addEdge(4,1,1)
  G.showGraph()
  G.graphContainsCycle(1)

Main6()