# Using readliness()
file1 = open('directions.txt', 'r')
Lines = file1.readlines()
 
# ******************************************
# PART 1 - Dive
# Calculate the horizontal position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?
# ******************************************
depth = 0
horizontal = 0
# Strips the newline character
for line in Lines:
    args = line.split() #split string into a list
    command = args[0]
    length = int(args[1])
    if command == "forward":
        horizontal += length
    elif command == "back":
        horizontal -= length
    elif command == "up":
        depth -= length
    elif command == "down":
        depth += length


print(f"depth horizontal product: {depth*horizontal}")