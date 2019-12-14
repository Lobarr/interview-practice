class Graph:
  class Node:
    def __init__(self, id):
      self.id = id
      self.adjacentNodes = []

    def isAdjacent(self, id):
      return id in self.adjacentNodes

    def getId(self):
      return self.id

  def __init__(self):
    self.nodeLookup = {}

  def _getNode(self, id):
    if id in self.nodeLookup:
      return self.nodeLookup[id]
    return None
  
  def addEdge():
    pass


