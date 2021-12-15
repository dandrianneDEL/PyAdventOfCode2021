def readfile() -> list[list[int]]:
    file1 = open('smoke.txt', 'r')

    grid = []
    for line in file1:
        row = []
        grid.append(row)
        for num in line:
            if num == "\n":
                continue
            row.append(int(num))

    print(grid)
    return grid