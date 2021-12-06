import filehelper

fileresult = filehelper.read_file()

class CarthesianGrid:
    gridSize = 10
    vents = []
    grid = []

    def __init__(self, vents, gridSize):
        self.vents = []
        self.gridSize = gridSize
        for vent in vents:
            print(vent)
            startCoords = Coords(vent[0][0], vent[0][1])
            endCoords = Coords(vent[1][0], vent[1][1])
            
            self.vents.append(Vents(startCoords, endCoords))
        self.calculateVentGrid()

    def calculateVentGrid(self):
        # init 0 grid
        for x in range(self.gridSize+1):
            self.grid.append([0] * (self.gridSize+1))

        # add 1 for each vent coord
        for vent in self.vents:
            ventCoords = vent.getCoordinates()
            for ventCoord in ventCoords:
                # print(f"incrementing {ventCoord.x} {ventCoord.y} (max = {self.gridSize})")
                self.grid[ventCoord.x][ventCoord.y] += 1

        self.print()

    def countPointsAboveThreshold(self, threshold):
        count = 0
        for x in self.grid:
            debug = ""
            for y in x:
                debug += f"{y} "
                if y >= 2:
                    count += 1
            # print(debug)
        return count

    def print(self):
        for x in self.grid:
            debug = ""
            for y in x:
                debug += f"{y} "
            print(debug)

class Vents:
    startCoords = None
    endCoords = None
    isHorizontal = False
    isDiagonal = False
    length = 1

    def __init__(self, start, end):
        self.startCoords = start
        self.endCoords = end
        if start.x == end.x:
            self.isHorizontal = True
            self.isDiagonal = False
            self.length = end.y - start.y
        else: 
            if start.y != end.y:
                self.isDiagonal = True
            self.isHorizontal = False
            self.length = end.x - start.x
    
    def getCoordinates(self):
        result = []
        #horizontal ascension
        if self.isHorizontal:
            if(self.startCoords.y <= self.endCoords.y):
                for y in range(self.startCoords.y, self.endCoords.y+1):
                    result.append(Coords(self.startCoords.x, y))
            else:
                for y in range(self.endCoords.y, self.startCoords.y+1):
                    result.append(Coords(self.startCoords.x, y))
        #diagonal ascension
        elif self.isDiagonal:
            count = 0
            if(self.startCoords.x <= self.endCoords.x):
                for x in range(self.startCoords.x, self.endCoords.x+1):
                    if self.startCoords.y <= self.endCoords.y:
                        result.append(Coords(x, self.startCoords.y+count))
                    else:
                        result.append(Coords(x,self.startCoords.y - count))
                    count += 1
            else:
                for x in range(self.endCoords.x, self.startCoords.x+1):
                    if self.startCoords.y <= self.endCoords.y:
                        result.append(Coords(self.startCoords.x-count, self.startCoords.y+count))
                    else:
                        result.append(Coords(self.startCoords.x-count, self.startCoords.y-count))
                    count += 1
            
        #vertical ascension
        else:
            if(self.startCoords.x <= self.endCoords.x):
                for x in range(self.startCoords.x, self.endCoords.x+1):
                    result.append(Coords(x, self.startCoords.y))
            else:
                for x in range(self.endCoords.x, self.startCoords.x+1):
                    result.append(Coords(x, self.startCoords.y))
        debug = "["
        for c in result:
            debug += f"{{x:{c.x} y:{c.y}}} "
        print(f"{debug}]")
        return result

class Coords:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

# ******************************************
# PART 1 - Vents
# You need to determine the number of points where at least two lines overlap.
# At how many points do at least two lines overlap?
# ******************************************
grid = CarthesianGrid(fileresult.ventCoords, fileresult.gridSize)
overlapCount = grid.countPointsAboveThreshold(2)
print(f"{overlapCount} cells above 2")