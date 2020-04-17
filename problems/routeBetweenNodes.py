from queue import Queue

class Node:
  def __init__(self, vertex):
    self.vertex = vertex
    self.neighbours = []

  def addNeighbour(self, neighbour):
    self.neighbours.append(neighbour)

  def neighboursCount(self):
    return len(self.neighbours)

  def getNeighbours(self):
    return self.neighbours

  def getVertex(self):
    return self.vertex

  def __eq__(self, check):
    return (
      check.getVertex() == self.getVertex() 
      and check.getNeighbours() == self.getNeighbours()
    )

class Graph:
  def __init__(self):
    self.vertices = []

  def addVertex(self, vertex: Node):
    self.vertices.append(vertex)

  def getVertices(self):
    return self.vertices

  def verticesCount(self):
    return len(self.vertices)

  def breadthFirstSearch(self, start: Node, end: Node):
    if start == end:
      return True
    
    queue = Queue()
    visited = { start.getVertex(): True }
    queue.put(start)
    
    while not queue.empty():
      cur = queue.get()
      for neighbour in cur.getNeighbours():
        if neighbour.getVertex() not in visited:
          if neighbour == end:
            return True
          visited[neighbour.getVertex()] = True
          queue.put(neighbour)
          
    return False
      
if __name__ == '__main__':
    graph = Graph()

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    a.addNeighbour(b)
    a.addNeighbour(c)
    b.addNeighbour(d)
    c.addNeighbour(e)

    for vertex in [a,b,c,d,e]:
      graph.addVertex(vertex)

    print(graph.breadthFirstSearch(a, e))

