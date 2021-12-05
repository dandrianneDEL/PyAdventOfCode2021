# Using readlines()
file1 = open('binaries.txt', 'r')
lines = file1.readlines()

def identify_bit_1_occurances_at_index(lines, bitIndex):
    bit1Occurances = 0
    # Strips the newline character
    for line in lines:
        binary = int(line, 2) # int base 2 ==> binary: src https://www.kite.com/python/answers/how-to-convert-binary-to-string-in-python
        if binary >> bitIndex & 1: # if bit is equal to 1
            bit1Occurances += 1 # count it in the bit position
    return bit1Occurances

# ******************************************
# PART 2 - Oxygen and Scrubber ratings
# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together.
# What is the life support rating of the submarine?
# ******************************************
filteredOxygenBinaries = lines
filteredScrubberBinaries = lines
bitsCount = len(lines[0].rstrip("\n"))
print(bitsCount, "bitscount")
for i in range(bitsCount):
    bitIndex = bitsCount - i -1 # this took another half hour to find, lol
    totalLinesOxygen = len(filteredOxygenBinaries)
    averageLinesOxygen = totalLinesOxygen/2

    bit1OccurancesAtIndexOxygen = identify_bit_1_occurances_at_index(filteredOxygenBinaries, bitIndex)
    if bit1OccurancesAtIndexOxygen >= averageLinesOxygen:
        bitOxygenCriteria = 1
    else:
        bitOxygenCriteria = 0
    if len(filteredOxygenBinaries) != 1: 
        filteredOxygenBinaries = list(filter(lambda line: (int(line, 2) >> bitIndex & 1) == bitOxygenCriteria, filteredOxygenBinaries))

    totalLinesScrubber = len(filteredScrubberBinaries)
    averageLinesScrubber = totalLinesScrubber/2

    bit1OccurancesAtIndexScrubber = identify_bit_1_occurances_at_index(filteredScrubberBinaries, bitIndex)
    if bit1OccurancesAtIndexScrubber >= averageLinesScrubber:
        bitScrubberCriteria = 0
    else:
        bitScrubberCriteria = 1

    if len(filteredScrubberBinaries) != 1:
        filteredScrubberBinaries = list(filter(lambda line: (int(line, 2) >> bitIndex & 1) == bitScrubberCriteria, filteredScrubberBinaries))

    print(filteredScrubberBinaries)
    print(len(filteredScrubberBinaries))
    if len(filteredOxygenBinaries) == 1 and len(filteredScrubberBinaries) == 1:
        break

oxygenRating = filteredOxygenBinaries[0]
scrubberRating = filteredScrubberBinaries[0]
oxygenRatingInt = int(oxygenRating, 2)
scrubberRatingInt = int(scrubberRating, 2)
print(f"oxygen {oxygenRatingInt}({oxygenRating}) scrubber {scrubberRatingInt}({scrubberRating})")
print(f"life support rating: {oxygenRatingInt*scrubberRatingInt}")