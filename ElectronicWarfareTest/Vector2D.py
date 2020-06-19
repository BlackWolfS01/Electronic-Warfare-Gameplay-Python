class Vector2D(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def printCoordinates(self):
    print("x, y: " + str(self.x) +", " + str(self.y))