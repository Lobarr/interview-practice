from queue import Queue

class Can:
  def __init__(self, capacity):
    self.capacity = capacity

  def getCapacity(self):
    return self.capacity

  def setCapacity(self, capacity):
    self.capacity = capacity

def wateringCans(plants, capacity):  
  refills = 0
  myCan = Can(capacity)
  friendCan = Can(capacity)
  nextCanQueue = Queue()
  nextCanQueue.put(myCan)
  nextCanQueue.put(friendCan)

  while len(plants) > 0:
    nextCan = nextCanQueue.get()
    plant = None
    
    if nextCan is myCan:
      plant = plants[0]
      plants.pop(0)
      nextCanQueue.put(myCan)
    else:
      plant = plants[-1]
      plants.pop(-1)
      nextCanQueue.put(friendCan)

    if nextCan.getCapacity() <= plant:
      refills += 1
      myCan.setCapacity(capacity)
      friendCan.setCapacity(capacity)
    nextCan.setCapacity(nextCan.getCapacity() - plant)

  return refills
