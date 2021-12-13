import filehelper
signalPairings = filehelper.read_file()

class SignalPairing:
    uniqueSignalCombinations = [2, 3, 4, 7]
    signals = []
    numbers = []

    def __init__(self, signalPairing):
        self.signals = signalPairing[0]
        self.numbers = signalPairing[1]

    def count_unique_segments(self):
        count = 0        
        for num in self.numbers:
            print(f"{num} ({len(num)}) is in unique segments 2, 3, 4 or 7 {len(num) in self.uniqueSignalCombinations}")
            if len(num) in self.uniqueSignalCombinations:
                count += 1
        return count

# ******************************************
# PART 1 - Unique segment alignment
# Counting only digits in the output values (the part after | on each line), in the above example 
# In the output values, how many times do digits 1, 4, 7, or 8 appear?
# ******************************************
count = 0
for signalPairing in signalPairings:
    pairing = SignalPairing(signalPairing)
    count += pairing.count_unique_segments()

print(f"unique number segment combinations : {count}")