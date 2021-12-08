import math
file1 = open('crabs.txt', 'r')

crabline = file1.readline()
crabs = []
for crab in crabline.split(","):
    crabs.append(int(crab))

class Line:
    isMovingLeft = False
    isMovingRight = False
    crabs = []
    middleRight = -1
    middleLeft = -1
    middleCrab = -1

    line = -1
    def __init__(self, crabs):
        crabs.sort()
        self.crabs = crabs
        
        crabCount = len(self.crabs)
        middle = int(crabCount/2)
        avg = self.calculate_average()
        if crabCount % 2 == 1:
            self.middleRight = middle
            self.middleLeft = middle+1
            
            if crabs[self.middleLeft] < avg:
                self.isMovingLeft = False
                self.isMovingRight = True
            elif crabs[self.middleRight] > avg:
                self.isMovingLeft = True
                self.isMovingRight = False
            else:
                self.isMovingLeft = True
                self.isMovingRight = True
        else:
            self.middleCrab = crabs[middle]

            if self.middleCrab < avg:
                self.isMovingLeft = False
                self.isMovingRight = True
            else:
                self.isMovingLeft = True
                self.isMovingRight = False

    def calculate_average(self):
        avg = 0
        for crab in self.crabs:
            avg += crab
        avg /= len(crabs)
        return avg

    def move(self):
        fuelSpent = 0

        if self.middleCrab != -1:
            fuelSpent = self.moveToLine(self.middleCrab)
            self.line = self.middleCrab

        if self.isMovingLeft:
            if self.middleLeft != -1:
                fuelSpent = self.moveToLine(self.middleLeft)
                self.line = self.middleLeft
        
        if self.isMovingRight:
            if self.middleRight != -1:
                fuelRight = self.moveToLine(self.middleRight)
                if fuelRight < fuelSpent:
                    fuelSpent = fuelRight
                    self.line = self.middleRight
                
        return fuelSpent

    def moveToLine(self, lineToMoveTo):
        fuelSpent = 0
        for crab in self.crabs:
            fuel = crab - lineToMoveTo
            if fuel < 0:
                fuel *= -1
            fuelSpent += fuel
        return fuelSpent

    def print(self, days):
        text = f"After {days} days"
        for fishy in self.crabs:
            text+= f",{fishy.daysUntilPop}"
        print(text)

# ******************************************
# PART 1 - Crab alignment
# Determine the horizontal position that the crabs can align to using the least fuel possible. 
# How much fuel must they spend to align to that position?
# ******************************************
line = Line(crabs)
fuelSpent = line.move()

print(f"crabs spent {fuelSpent} moving to line : {line.line}")