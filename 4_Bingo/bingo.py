import filehelper

fileresult = filehelper.read_file()
print(fileresult.numbers)
print(fileresult.boards)

class Board:
    board = [] # list of list of cells

    # init method or constructor 
    def __init__(self, board):
        self.board = []
        for x in range(len(board)):
            row = board[x]
            self.board.append([])
            for y in range(len(row)):
                val = row[y]
                cell = Cell(x, y, val)
                self.board[x].append(cell)
    
    def mark_number(self, number):
        for row in self.board:
            for cell in row:
                if cell.val == number:
                    cell.mark()

    def check_is_complete(self):
        for row in self.board:
            for y in range(len(row)):
                cell = row[y]
                if not cell.isMarked :
                    break # this row has an unmarked one and is not complete, check next
                if y == len(row)-1:
                    return True # this row is completed, and so the board is

        colCount = len(self.board[0])-1
        for y in range(colCount):
            # print(f"checking col {y} in {self.board}")
            unmarkedCellsForCol = list(filter(lambda row: not row[y].isMarked, self.board))
            if(len(unmarkedCellsForCol) == 0):
                return True  # this col is completed, and so the board is

        return False

    def sum_unmarked(self):
        sum = 0
        for row in self.board:
            for cell in row:
                if not cell.isMarked :
                    sum += cell.val
        return sum

    def print(self):
        for row in self.board:
            txt = ""
            for cell in row:
                if cell.isMarked:
                    txt += f"*{cell.val} "
                else:
                    txt += f"{cell.val} "
            print(txt)
        print("-----")

class Cell:
    x = 0
    y = 0
    val = 0
    isMarked = 0

    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def mark(self):
        self.isMarked = 1

# ******************************************
# PART 1 - Bingo
# Start by finding the sum of all unmarked numbers on that board. 
# Then, multiply that sum by the number that was just called when the board won
# What will your final score be if you choose that board?
# ******************************************
boards = []
for board in fileresult.boards:
    boards.append(Board(board))

for num in fileresult.numbers:
    print("*****")
    for board in boards:
        board.mark_number(num)
        board.print()
        if(board.check_is_complete()):
            unmarkedSum = board.sum_unmarked()
            print(f"unmarkedSum {unmarkedSum} * {num}")
            print(f"final score: {unmarkedSum*num}")
            exit()