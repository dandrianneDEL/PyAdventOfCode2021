file1 = open('fish.txt', 'r')

fishline = file1.readline()
fish = []
for fishy in fishline.split(","):
    fish.append(int(fishy))

class School:
    fish: []
    def __init__(self, fish):
        self.fish = []
        for fishy in fish:
            self.fish.append(LanternFish(fishy))

    def pass_day(self):
        newFishies = []
        for fishy in self.fish:
            newFishy = fishy.decrement_and_maybe_hatch()
            if(newFishy != None):
                newFishies.append(newFishy)
        
        for newFishy in newFishies:
            self.fish.append(newFishy)

    def print(self, days):
        text = f"After {days} days"
        for fishy in self.fish:
            text+= f",{fishy.daysUntilPop}"
        print(text)

class LanternFish:
    daysUntilPop = 0

    def __init__(self, daysUntilPop):
        self.daysUntilPop = daysUntilPop

    def decrement_and_maybe_hatch(self):
        if(self.daysUntilPop > 0):
            self.daysUntilPop -= 1
            return None
        else:
            self.daysUntilPop = 6
            return LanternFish(8)

# ******************************************
# PART 1 - LanternFish
# Find a way to simulate lanternfish. 
# How many lanternfish would there be after 80 days?
# ******************************************
school = School(fish)

for day in range(80):
    school.pass_day()
    school.print(day)

print(f"Lanternfish after 80 days : {len(school.fish)}")