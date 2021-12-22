import filehelper
fileResult = filehelper.readfile()

class Matrix:
    cells: list[list[bool]]
    maxX: int
    maxY: int
    def __init__(self, sizeX:int, sizeY:int) -> None:
        self.cells = []
        self.maxX = sizeX
        self.maxY = sizeY
        # print(f"INIT matrix {sizeX}x{sizeY}")
        for y in range(sizeY+1):
            row = [False] * (sizeX+1)
            self.cells.append(row)

    def fill_coords(self, coords:list[int]) -> None:
        for carthesianCoordinate in coords:
            x = carthesianCoordinate[0]
            y = carthesianCoordinate[1]
            self.cells[y][x] = True

    def subselect(self, xStart:int, yStart:int, xMax:int, yMax:int, translateX: int, translateY: int) -> 'Matrix':
        print(f"x={xStart}-{xMax}, y={yStart}-{yMax}")
        newMatrix = Matrix(xMax-xStart, yMax-yStart)
        coords = []
        for x in range(xStart,xMax+1):
            for y in range(yStart, yMax+1):
                if self.cells[y][x]:
                    coords.append([x-translateX, y-translateY])
        print(f"part coords(translateY={translateY}): {coords}")
        newMatrix.fill_coords(coords)
        return newMatrix

    def merge_y(self, half2:'Matrix')->'Matrix':
        merged = Matrix(self.maxX, self.maxY-1)
        coords = []
        
        # populate cell if either folds are populated
        for x in range(self.maxX+1):
            for y in range(self.maxY):
                if self.cells[y][x] or half2.cells[half2.maxY-y][x]:
                    coords.append([x,y])
        merged.fill_coords(coords)
        
        return merged

    def merge_x(self, half2:'Matrix')->'Matrix':
        merged = Matrix(self.maxX-1, self.maxY)
        coords = []
        for x in range(self.maxX):
            for y in range(self.maxY+1):
                if self.cells[y][x] or half2.cells[y][half2.maxX-x]:
                    coords.append([x,y])
        merged.fill_coords(coords)

        return merged

    def fold(self, fold) -> 'Matrix':
        if fold[0] == 'y':
            yAxisToFold = fold[1]
            self.print(yAxisToFold, -1)
            merged = self.fold_y(yAxisToFold)
        else:
            xAxisToFold = fold[1]
            self.print(-1, xAxisToFold)
            merged = self.fold_x(xAxisToFold)
        merged.print(-1, -1)
        return merged

    def fold_y(self, y:int) -> 'Matrix':
        half1 = self.subselect(0, 0, self.maxX, y, 0, 0)
        half2 = self.subselect(0, y, self.maxX, self.maxY, 0, y)
        return half1.merge_y(half2)

    def fold_x(self, x:int) -> 'Matrix':
        half1 = self.subselect(0, 0, x, self.maxY, 0, 0)
        half2 = self.subselect(x, 0, self.maxX, self.maxY, x, 0)
        return half1.merge_x(half2)

    def print(self, splitY:int, splitX:int) -> None:
        for y in range(len(self.cells)):
            row = self.cells[y]
            txt = ""
            for x in range(len(row)):
                flag = row[x] 
                if y == splitY:
                    txt += "-"
                elif x == splitX:
                    txt += "|"
                elif flag:
                    txt += "#"
                else:
                    txt += f"."
            print(txt)

# ******************************************
# PART 2 - Fold plastic transparent sheet
# Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.
# What code do you use to activate the infrared thermal imaging camera system?
# ******************************************
matrix = Matrix(fileResult.maxX, fileResult.maxY)
matrix.fill_coords(fileResult.coords)

# Perform folds
for fold in fileResult.folds: 
    print(f"performing fold {fold}")
    matrix = matrix.fold(fold)