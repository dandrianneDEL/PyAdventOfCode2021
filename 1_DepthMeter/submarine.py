MIN_MAX = float('inf') * -1

# Using readliness()
file1 = open('depth_readings.txt', 'r')
Lines = file1.readlines()
 
# ******************************************
# PART 1 - Depth readings
# How many measurements are larger than the previous measurement?
# ******************************************
count = -1
lastVal = MIN_MAX
# Strips the newline character
for line in Lines:
    if float(line) > lastVal:
        count += 1
    lastVal = float(line)

print(f"depth increases {count}")