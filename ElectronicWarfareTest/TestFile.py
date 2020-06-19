from Vector2D import Vector2D

columnsMax = 10
columnsMin = -10
rowsMax = 10
rowsMin = -10
grid = [[Vector2D(x,y) for x in range(columnsMin, columnsMax)] for y in range(rowsMin, rowsMax)]

for x in range(len(grid)):
  for y in range(len(grid[x])):
    grid[x][y].printCoordinates()
