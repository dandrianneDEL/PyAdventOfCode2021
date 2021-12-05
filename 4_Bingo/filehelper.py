def read_file():
    # Using readlines()
    file1 = open('numbers.txt', 'r')

    num_lines = sum(1 for line in file1)
    if num_lines % 6 != 1:
        raise FileFormatNotSupportedError

    file1 = open('numbers.txt', 'r')
    numbersLine = file1.readline() # https://stackoverflow.com/a/4796785

    boards = []
    for line in file1:
        if len(line.rstrip("\n")) == 0:
            lastBoard = []
            boards.append(lastBoard)
            continue

        row = []
        numbers = line.split(" ")
        for num in numbers:
            if len(num) == 0:
                continue
            row.append(int(num))
        lastBoard.append(row)

    return FileResult(numbersLine, boards)

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class FileFormatNotSupportedError(Error):
    """Raised when there are an unexpected number of lines in the input file"""
    pass

class FileResult:
    boards = []
    numbers = []

    def __init__(self, numbersLine, boards):
        for num in numbersLine.split(","):
            if len(num) == 0:
                continue
            self.numbers.append(int(num))
        self.boards = boards