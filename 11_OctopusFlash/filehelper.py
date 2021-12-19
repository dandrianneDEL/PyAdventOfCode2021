def readfile() -> list[list[int]]:
    file1 = open('octo.txt', 'r')
    result = []
    for line in file1:
        row = []
        for num in line.strip():
            row.append(int(num))    
        result.append(row)

    print(result)
    return result