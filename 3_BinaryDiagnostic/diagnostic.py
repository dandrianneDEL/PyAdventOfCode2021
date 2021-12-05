# Using readlines()
file1 = open('binaries.txt', 'r')
Lines = file1.readlines()

"""Set the binary for each occurance to 1 if it matches the frequency criteria (having bit1 occurances most or least frequent above the average line count)"""
def generateFrequentBinary(bit1OccurancesList, average, mostFrequent):
    mostFrequentBinary = 0b0
    for bitIndex in range(len(bit1OccurancesList)):
        bitToSet = 0
        if(bit1OccurancesList[bitIndex] > average and mostFrequent or (not mostFrequent and bit1OccurancesList[bitIndex] < average)):
            bitToSet = 1
        mostFrequentBinary = set_bit(mostFrequentBinary, bitIndex, bitToSet)
    return mostFrequentBinary
        
# src: https://stackoverflow.com/a/12174051
"""Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
def set_bit(v, index, x):
    mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
    v &= ~mask          # Clear the bit indicated by the mask (if x is False)
    if x:
        v |= mask       # If x was True, set the bit indicated by the mask.
    return v            # Return the result, we're done.
 
# ******************************************
# PART 1 - Diagnostic
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. 
# What is the power consumption of the submarine?
# ******************************************
bit1OccurancesList = ()
totalLines = 0
# Strips the newline character
for line in Lines:
    # first line only: init list with 0 for each char of the binary
    if len(bit1OccurancesList) == 0:
        bit1OccurancesList = [0] * (len(line)-1) # this -1 here costed me an hour to debug, lol Python

    binary = int(line, 2) # int base 2 ==> binary: src https://www.kite.com/python/answers/how-to-convert-binary-to-string-in-python
    for bitIndex in range(len(line)):
        if binary >> bitIndex & 1: # if bit is equal to 1
            bit1OccurancesList[bitIndex] += 1 # count it in the bit position
            print(f"The {bitIndex}th bit is '1', this index has been '1' {bit1OccurancesList[bitIndex]} times")
    print(f"{bit1OccurancesList} bit 1 occurances counts")
    totalLines += 1

averageLines = totalLines/2
gamma = generateFrequentBinary(bit1OccurancesList, averageLines, True)
epsilon = generateFrequentBinary(bit1OccurancesList, averageLines, False)

print(f"gamma {int(gamma)}({bin(gamma)}) epsilon {int(epsilon)}({bin(epsilon)})")
print(f"power consumption: {int(gamma)*int(epsilon)}")