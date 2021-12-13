import filehelper
signalPairings = filehelper.read_file()

import keyvalidator

class NumberTheory:
    numberKey: keyvalidator.NumberKey
    def __init__(self, numberKey):
        self.numberKey = numberKey

    def stringify(self, numbers):
        txt = ""
        for num in numbers:
            txt += num
        return txt

    def print(self, top, tr, tl, cent, br, bl, bot):
        txt = f" {top}{top}{top}{top} \n"
        txt += f"{tl}    {tr}\n"
        txt += f"{tl}    {tr}\n"
        txt += f" {cent}{cent}{cent}{cent} \n"
        txt += f"{bl}    {br}\n"
        txt += f"{bl}    {br}\n"
        txt += f" {bot}{bot}{bot}{bot} "

        print(txt) 

class OneTheory(NumberTheory):
    def __init__(self, numbers, numberKey:keyvalidator.NumberKey):
        super().__init__(numberKey)
        numberKey.add_to_not_top_mask(numbers)
        numberKey.add_to_top_right(numbers)
        numberKey.add_to_not_center_mask(numbers)
        numberKey.add_to_bottom_right(numbers)
        numberKey.add_to_not_bottom_mask(numbers)
        numberKey.add_to_not_bottom_left_mask(numbers)
        numberKey.add_to_not_top_left_mask(numbers)

    def print(self):
        tr = super().stringify(self.numberKey.topRight)
        br = super().stringify(self.numberKey.bottomRight)
        super().print(".", tr, ".", ".", br, ".", ".")

class FourTheory(NumberTheory):
    def __init__(self, numbers, numberKey:keyvalidator.NumberKey):
        super().__init__(numberKey)
        numberKey.add_to_not_top_mask(numbers)
        numberKey.add_to_top_right(numbers)
        numberKey.add_to_center(numbers)
        numberKey.add_to_bottom_right(numbers)
        numberKey.add_to_not_bottom_mask(numbers)
        numberKey.add_to_not_bottom_left_mask(numbers)
        numberKey.add_to_top_left(numbers)

    def print(self):
        tr = super().stringify(self.numberKey.topRight)
        tl = super().stringify(self.numberKey.topLeft)
        cent = super().stringify(self.numberKey.center)
        br = super().stringify(self.numberKey.bottomRight)
        super().print(".", tr, tl, cent, br, ".", ".")

class SevenTheory(NumberTheory):
    def __init__(self, numbers, numberKey:keyvalidator.NumberKey):
        super().__init__(numberKey)
        numberKey.add_to_top(numbers)
        numberKey.add_to_top_right(numbers)
        numberKey.add_to_not_center_mask(numbers)
        numberKey.add_to_bottom_right(numbers)
        numberKey.add_to_not_bottom_mask(numbers)
        numberKey.add_to_not_bottom_left_mask(numbers)
        numberKey.add_to_not_top_left_mask(numbers)

    def print(self):
        top = super().stringify(self.numberKey.top)
        tr = super().stringify(self.numberKey.topRight)
        br = super().stringify(self.numberKey.bottomRight)
        super().print(top, tr, ".", ".", br, ".", ".")

class EightTheory(NumberTheory):
    def __init__(self, numbers, numberKey:keyvalidator.NumberKey):
        super().__init__(numberKey)
        numberKey.add_to_top(numbers)
        numberKey.add_to_top_right(numbers)
        numberKey.add_to_center(numbers)
        numberKey.add_to_bottom_right(numbers)
        numberKey.add_to_bottom(numbers)
        numberKey.add_to_bottom_left(numbers)
        numberKey.add_to_top_left(numbers)

    def print(self):
        top = super().stringify(self.numberKey.top)
        tr = super().stringify(self.numberKey.topRight)
        tl = super().stringify(self.numberKey.topLeft)
        cent = super().stringify(self.numberKey.center)
        br = super().stringify(self.numberKey.bottomRight)
        bl = super().stringify(self.numberKey.bottomLeft)
        bot = super().stringify(self.numberKey.bottom)
        super().print(top, tr, tl, cent, br, bl, bot)
        
    def print_nots(self):
        top = super().stringify(self.numberKey.notTop)
        tr = super().stringify(self.numberKey.notTopRight)
        tl = super().stringify(self.numberKey.notTopLeft)
        cent = super().stringify(self.numberKey.notCenter)
        br = super().stringify(self.numberKey.notBottomRight)
        bl = super().stringify(self.numberKey.notBottomLeft)
        bot = super().stringify(self.numberKey.notBottom)
        super().print(top, tr, tl, cent, br, bl, bot)

class SignalPairing:
    signals = []
    numbers = []

    def __init__(self, signalPairing):
        self.signals = signalPairing[0]
        self.numbers = signalPairing[1]

# ******************************************
# PART 2 - Number deduction
# Counting only digits in the output values (the part after | on each line), in the above example 
# In the output values, how many times do digits 1, 4, 7, or 8 appear?
# ******************************************
count = 0
for signalPairing in signalPairings:
    numKey = keyvalidator.NumberKey([],[],[],[],[],[],[] )
    pairing = SignalPairing(signalPairing)
    eightTheory = EightTheory(list(filter(lambda x: len(x) == 7, pairing.signals)), numKey)
    # eightTheory.print_nots()
    # print("---8---")
    fourTheory = FourTheory(list(filter(lambda x: len(x) == 4, pairing.signals)), numKey)
    # eightTheory.print_nots()
    # print("---4---")
    sevenTheory = SevenTheory(list(filter(lambda x: len(x) == 3, pairing.signals)), numKey)
    # eightTheory.print_nots()
    # print("---7---")
    oneTheory = OneTheory(list(filter(lambda x: len(x) == 2, pairing.signals)), numKey)
    # eightTheory.print_nots()
    # print("---1---")
    # numKey.eliminate_possibilities_based_of_mask()
    # eightTheory.print()

    validator = keyvalidator.KeyValidator(numKey, pairing.signals)
    eightTheory.numberKey = validator.validate_key()
    eightTheory.print()
    txt = f"Num decoded: "
    i = len(pairing.numbers)-1
    for numberSignals in pairing.numbers:
        decodedNumber = eightTheory.numberKey.decode_number(numberSignals)
        count += decodedNumber * pow(10,i)
        txt += f"{decodedNumber}"
        i -= 1
    print(txt)

print(f"total : {count}")