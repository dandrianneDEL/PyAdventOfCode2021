# Using readliness()
file1 = open('directions.txt', 'r')
Lines = file1.readlines()

# ******************************************
# PART 2 - Aim
# In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0.
# What do you get if you multiply your final horizontal position by your final depth?
# ******************************************
aim = 0
depth = 0
horizontal = 0
# Strips the newline character
for line in Lines:
    args = line.split() #split string into a list
    command = args[0]
    length = int(args[1])
    print(line)
    if command == "forward":
        horizontal += length
        depth += length * aim
    elif command == "back":
        horizontal -= length
        depth -= length * aim
    elif command == "up":
        aim -= length
    elif command == "down":
        aim += length


print(f"depth horizontal aimed product: {depth*horizontal}")