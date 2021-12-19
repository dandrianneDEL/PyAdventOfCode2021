opening_chars = ['{', '(', '[', '<']
closing_chars = ['}', ')', ']', '>']

class FileResult:
    corrupted: list[str]
    incomplete: list[str]

    def __init__(self) -> None:
        self.corrupted = []
        self.incomplete = []
    
    def add_line(self, line) -> None:
        line = line.strip()
        # if len(line) % 2 != 0:
        #     self.incomplete.append(line)
        # else:
        #     openingChars = list(filter(lambda c: c in opening_chars, line))
        #     closingChars = list(filter(lambda c: c in opening_chars, line))
        #     if len(openingChars) != len(closingChars):
        #         self.incomplete.append(line)
        #     else:
        self.corrupted.append(line)

def readfile() -> FileResult:
    file1 = open('syntax.txt', 'r')

    result = FileResult()
    for line in file1:
        result.add_line(line)
    print(result.corrupted)
    return result