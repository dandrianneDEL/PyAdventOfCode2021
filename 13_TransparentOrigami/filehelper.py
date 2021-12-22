class FileResult:
    maxX:int
    maxY:int
    coords: list[tuple[int]]
    folds: dict
    def __init__(self, coords:list[tuple[int]], folds: dict, maxX:int, maxY:int) -> None:
        self.coords = coords
        self.folds = folds
        self.maxX = maxX
        self.maxY = maxY

def readfile() -> FileResult:
    file1 = open('origami.txt', 'r')
    coords = []
    folds = []
    maxX = 0
    maxY = 0
    for line in file1:
        if ',' in line:
            parts = line.split(',')
            x = int(parts[0])
            y = int(parts[1].strip())
            if maxX < x:
                maxX = x
            if maxY < y:
                maxY = y
            coords.append((x,y))
        elif '=' in line:
            parts = line.split('=')
            xOrY = parts[0]
            i = parts[1].strip()
            if xOrY.endswith('x'):
                folds.append(('x', int(i)))
            else:
                folds.append(('y', int(i)))

    return FileResult(coords, folds, maxX, maxY)