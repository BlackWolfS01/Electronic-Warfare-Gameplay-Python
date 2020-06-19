from Vector2D import Vector2D

class GridMap():

  def __init__(self, X_GridTotal, Y_GridTotal):
    self.X_GridTotal = X_GridTotal
    self.Y_GridTotal = Y_GridTotal
    self.X_Min = -(X_GridTotal % 2)
    self.X_Max = (X_GridTotal % 2)
    self.Y_Min = -(Y_GridTotal % 2) 
    self.Y_Max = (Y_GridTotal % 2)
    
    self.gridMap = [[Vector2D(x, y) for x in range(self.X_Min, self.X_Max)] for y in range(self.Y_Min, self.Y_Max)]