def read_file():
    # Using readlines()
    file1 = open('coords.txt', 'r')

    maxGridSize = 0
    ventCoords = []
    for line in file1:
        coords = line.split(" -> ")
        
        startCoords = coords[0].split(",")
        startX = int(startCoords[0])
        startY = int(startCoords[1])
        if(startX > maxGridSize):
            maxGridSize = startX
        if(startY > maxGridSize):
            maxGridSize = startY

        endCoords = coords[1].split(",")
        endX = int(endCoords[0])
        endY = int(endCoords[1])
        if(endX > maxGridSize):
            maxGridSize = endX
        if(endY > maxGridSize):
            maxGridSize = endY

        ventCoords.append([[startX, startY], [endX, endY]])

    return FileResult(ventCoords, maxGridSize)

class FileResult:
    ventCoords = []
    gridSize = 0

    def __init__(self, ventCoords, maxGridSize):
        self.ventCoords = ventCoords
        self.gridSize = maxGridSize