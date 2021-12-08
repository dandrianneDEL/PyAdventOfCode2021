MAX_INT = 9223372036854775807 # https://stackoverflow.com/a/7604981

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
        if self.isMovingLeft:
            if self.middleCrab != -1:
                fuelSpent = self.identify_best_line(self.middleCrab, True)

            if self.middleLeft != -1:
                fuelSpent = self.identify_best_line(self.middleLeft, True)
        
        if self.isMovingRight:
            if self.middleCrab != -1:
                fuelSpent = self.identify_best_line(self.middleCrab, False)
                
            if self.middleRight != -1:
                lineLeft = self.line
                fuelRight = self.identify_best_line(self.middleLeft, False)
                if fuelRight < fuelSpent:
                    fuelSpent = fuelRight
                else:
                    self.line = lineLeft
                
        return fuelSpent

    def identify_best_line(self, startIndex, isMovingLeft):
        pivot = startIndex
        fuelSpent = self.move_to_line(pivot)
        priorFuelSpent = MAX_INT
        
        while priorFuelSpent > fuelSpent:
            priorFuelSpent = fuelSpent
            if isMovingLeft:
                pivot -= 1
            else:
                pivot += 1 # moving right
            fuelSpentTest = self.move_to_line(pivot)
            print(f"{fuelSpent} spent to line {pivot} (prior: {priorFuelSpent}) moving left {isMovingLeft}")
            if fuelSpentTest < fuelSpent:
                fuelSpent = fuelSpentTest
            else:
                if isMovingLeft:
                    pivot += 1
                else:
                    pivot -= 1

        self.line = pivot
        return fuelSpent

    def move_to_line(self, lineToMoveTo):
        fuelSpent = 0
        for crab in self.crabs:
            steps = 0
            stepsAway = crab - lineToMoveTo
            if stepsAway < 0:
                stepsAway *= -1
            for n in range(stepsAway):
                fuelSpent += 1 + steps
                steps += 1
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