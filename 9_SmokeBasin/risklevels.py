import filehelper
grid = filehelper.readfile()

class Cell:
    number : int
    x : int
    y : int
    isLowPoint = False
    topCell = None
    leftCell = None
    bottomCell = None
    rightCell = None

    def __init__(self, x, y, num):
        self.isLowPoint = False
        self.x = x
        self.y = y
        self.number = num

    def set_neighbors(self, grid):
        if self.x > 0:
            self.topCell = grid[self.x-1][self.y]
        else:
            self.topCell = None
            
        if self.x+1 < len(grid):
            self.bottomCell = grid[self.x+1][self.y]
        else:
            self.bottomCell = None
        if self.y+1 < len(grid[self.x]):
            self.rightCell = grid[self.x][self.y+1]
        else:
            self.rightCell = None
        if self.y > 0:
            self.leftCell = grid[self.x][self.y-1]
        else:
            self.leftCell = None
        self.determine_is_low_point()
    
    def determine_is_low_point(self):
        if self.topCell == None:
            isTopHigher = True
        else:
            isTopHigher = self.topCell.number > self.number
            if isTopHigher:
                print(f"{self.x}, {self.y}: top {self.topCell.number} > {self.number}")
        if self.rightCell == None:
            isRightHigher = True
        else:
            isRightHigher = self.rightCell.number > self.number
            if isRightHigher:
                print(f"{self.x}, {self.y}: right {self.rightCell.number} > {self.number}")
        if self.bottomCell == None:
            isBottomHigher = True
        else: 
            isBottomHigher = self.bottomCell.number > self.number
            if isBottomHigher:
                print(f"{self.x}, {self.y}: bottom {self.bottomCell.number} > {self.number}")
        if self.leftCell == None:
            isLeftHigher = True
        else:
            isLeftHigher = self.leftCell.number > self.number
            if isLeftHigher:
                print(f"{self.x}, {self.y}: left {self.leftCell.number} > {self.number}")
        self.isLowPoint = isTopHigher and isRightHigher and isBottomHigher and isLeftHigher
        if self.isLowPoint:
            print(f"Lowpoint at {self.x}, {self.y} ({self.number})")

    def calc_risk_level(self) -> int:
        if(self.isLowPoint):
            return self.number + 1
        # mid-high points don't count
        return 0

# ******************************************
# PART 1 - Smoke basin
# Find all of the low points on your heightmap. 
# What is the sum of the risk levels of all low points on your heightmap?
# ******************************************
carthesianGrid:list[list[Cell]] = []
for x in range(len(grid)):
    row = []
    carthesianGrid.append(row)
    for y in range(len(grid[x])):
        val = grid[x][y]
        cell = Cell(x, y, val)
        row.append(cell)

count = 0
for row in carthesianGrid:
    for cell in row:
        cell.set_neighbors(carthesianGrid)
        if cell.isLowPoint:
            count += cell.calc_risk_level()

print(f"total low point risk: {count}")