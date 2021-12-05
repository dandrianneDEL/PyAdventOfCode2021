import filehelper

fileresult = filehelper.read_file()
print(fileresult.numbers)
print(fileresult.boards)

class Board:
    board = [] # list of list of cells
    isComplete = False

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
                    self.isComplete = True
                    debug = "row complete: "
                    for c in row:
                        debug += f"{c.val} "
                    print(debug)
                    return True # this row is completed, and so the board is

        colCount = len(self.board[0])
        for y in range(colCount):
            unmarkedCellsForCol = list(filter(lambda row: not row[y].isMarked, self.board))
            if(len(unmarkedCellsForCol) == 0):
                debug = "col complete: "
                for c in self.board:
                    debug += f"{c[y].val} "
                print(debug)
                self.isComplete = True
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
# PART 2 - Bingo Lose
# Figure out which board will win last. 
# Once it wins, what would its final score be?
# ******************************************
boards = []
for board in fileresult.boards:
    boards.append(Board(board))

completedBoards = 0
for num in fileresult.numbers:
    print(f"***{num}***")
    for board in boards:
        if(board.isComplete):
            continue
        board.mark_number(num)
        board.print()
        if(board.check_is_complete()):
            completedBoards += 1
            if len(boards) - completedBoards == 0:
                unmarkedSum = board.sum_unmarked()
                print(f"unmarkedSum {unmarkedSum} * {num}")
                print(f"final score: {unmarkedSum*num}")
                exit()