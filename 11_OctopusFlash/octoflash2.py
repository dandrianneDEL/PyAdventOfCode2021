import filehelper
octopuses = filehelper.readfile()

class Octopus:
    hasFlashed: bool
    energy: int
    neighbors = []

    def __init__(self, energy) -> None:
        self.hasFlashed = False
        self.neighbors = []
        self.energy = energy

    def increment(self) -> bool:
        self.energy += 1
        if self.energy > 9:
            self.flash()
        return self.hasFlashed

    def flash(self) -> None:
        self.hasFlashed = True
        self.energy = 0
        unflashedNeighbors = list(filter(lambda n: not n.hasFlashed, self.neighbors))
        for n in unflashedNeighbors:
            n.increment()

    def settle(self) -> None:
        if self.hasFlashed:
            self.energy = 0
        self.hasFlashed = False

def init_neighbours(octopuses:list[list[Octopus]]) -> list[list[Octopus]]:
    for x in range(len(octopuses)):
        for y in range(len(octopuses[x])):
            octopusToFetchNeighboursFor = octopuses[x][y]
            neighbors = []
            if x > 0: 
                # add left neighbor ref
                neighbors.append(octopuses[x-1][y])
                if y > 0:
                    # add top left neighbor ref
                    neighbors.append(octopuses[x-1][y-1])
                if y+1 < len(octopuses[x]):
                    # add bottom left neighbor ref
                    neighbors.append(octopuses[x-1][y+1])
            if y > 0:
                # add top neighbor ref
                neighbors.append(octopuses[x][y-1])
                if x+1 < len(octopuses):
                    # add top right neighbor ref
                    neighbors.append(octopuses[x+1][y-1])
            if x+1 < len(octopuses):
                # add right neighbor ref
                neighbors.append(octopuses[x+1][y])
                if y+1 < len(octopuses[x]):
                    # add bottom right neighbor ref
                    neighbors.append(octopuses[x+1][y+1])
            if y+1 < len(octopuses[x]):
                # add bottom neighbor ref
                neighbors.append(octopuses[x][y+1])
            octopusToFetchNeighboursFor.neighbors = neighbors

def step(allOctopuses:list[Octopus]) -> int:
    flashedOctopuses = list(filter(lambda o: o.increment(), allOctopuses))
    for octo in allOctopuses:
        octo.settle()

    return len(list(filter(lambda o: o.energy == 0, allOctopuses)))

def print_grid(octoGrid:list[list[Octopus]],i)->None:
    for row in octoGrid:
        txt = ""
        for octo in row:
            txt += f"{octo.energy}"
        print(txt)
    print(f"---{i}---")

# ******************************************
# PART 1 - Octopus Flashing
# Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. 
# How many total flashes are there after 100 steps?
# ******************************************
octoGrid = []
for octoline in octopuses:
    octoRow = []
    for octopusEnergy in octoline:
        octoRow.append(Octopus(octopusEnergy))
    octoGrid.append(octoRow)

octogrid = init_neighbours(octoGrid)

allOctopuses = [item for sublist in octoGrid for item in sublist]
s = 0
flashes = 0
while flashes != len(allOctopuses):
    flashes = step(allOctopuses)
    s += 1
    print_grid(octoGrid, s)
    print(f"flashes this step: {flashes}")

print(f"First step where all octopuses flash in sync: {s}")