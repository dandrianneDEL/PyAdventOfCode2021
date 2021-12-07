file1 = open('fish.txt', 'r')

fishline = file1.readline()
fish = []
for fishy in fishline.split(","):
    fish.append(int(fishy))

class School:
    fish: []
    def __init__(self, fish):
        self.fish = [0] * 9
        for fishy in fish:
            self.fish[fishy] += 1

    def pass_day(self, day):
        mod = day % 7
        weeFish = self.fish[8]
        self.fish[8] = self.fish[mod] # new wee fish born

        self.fish[mod] += self.fish[7] # young fish become adults
        self.fish[7] = weeFish # wee fish become young

    def print(self, days):
        text = f"After {days} days"
        for fishy in self.fish:
            text+= f",{fishy}"
        print(text)

    def sum(self):
        sum = 0
        for fishy in self.fish:
            sum+= fishy
        return sum

# ******************************************
# PART 2 - LanternFish
# Find a way to simulate lanternfish. 
# How many lanternfish would there be after 256 days?
# ******************************************
school = School(fish)

for day in range(256):
    school.pass_day(day)

print(f"Lanternfish after 256 days : {school.sum()}")