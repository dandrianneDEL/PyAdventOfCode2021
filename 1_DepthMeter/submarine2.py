MIN_MAX = float('inf') * -1

# Using readliness()
file1 = open('depth_readings.txt', 'r')
Lines = file1.readlines()

# ******************************************
# PART 2 - Sliding window
# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
# ******************************************
count = 0
a = MIN_MAX
b = a
c = a
lastSum = a
# Strips the newline character
for line in Lines:
    lastVal = float(line)
    if a == MIN_MAX:
        a = lastVal
    elif b == MIN_MAX:
        b = lastVal
    elif c == MIN_MAX:
        c = lastVal
    else:
        a = b
        b = c
        c = lastVal

    if c != MIN_MAX:
        slidingWindow = a+b+c
        if lastSum != MIN_MAX and lastSum < slidingWindow:
            count += 1
        lastSum = slidingWindow

print(f"sliding window increases {count}")