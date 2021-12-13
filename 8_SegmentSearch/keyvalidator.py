from typing import Text


class NumberKey:
    top = []
    topRight = []
    center = []
    bottomRight = []
    bottom = []
    bottomLeft = []
    topLeft = []

    notTop = []
    notTopRight = []
    notCenter = []
    notBottomRight = []
    notBottom = []
    notBottomLeft = []
    notTopLeft = []

    zeroSignals = []
    oneSignals = []
    twoSignals = []
    threeSignals = []
    # fourSignals = []
    fiveSignals = []
    sixSignals = []
    sevenSignals = []
    # eightSignals = []
    nineSignals = []

    def __init__(self, top = [], topRight = [], topLeft = [], center = [], bottomRight = [], bottomLeft = [], bottom = []) -> None:
        self.top = top
        self.topRight = topRight
        self.topLeft = topLeft
        self.center = center
        self.bottomRight = bottomRight
        self.bottomLeft = bottomLeft
        self.bottom = bottom

        self.notTop = []
        self.notTopLeft = []
        self.notTopRight = []
        self.notCenter = []
        self.notBottom = []
        self.notBottomLeft = []
        self.notBottomRight = []

        self.zeroSignals = []
        self.oneSignals = []
        self.twoSignals = []
        self.threeSignals = []
        self.fiveSignals = []
        self.sixSignals = []
        self.sevenSignals = []
        self.nineSignals = []
    
    def add_to_possibilities(self, signals, register):
        for signal in signals:
            for letter in signal:
                if letter not in register:
                    register.append(letter)

    def add_to_top(self, signals):
        self.add_to_possibilities(signals, self.top)
    def add_to_top_right(self, signals):
        self.add_to_possibilities(signals, self.topRight)    
    def add_to_center(self, signals):
        self.add_to_possibilities(signals, self.center)
    def add_to_bottom_right(self, signals):
        self.add_to_possibilities(signals, self.bottomRight)
    def add_to_bottom(self, signals):
        self.add_to_possibilities(signals, self.bottom)
    def add_to_bottom_left(self, signals):
        self.add_to_possibilities(signals, self.bottomLeft)
    def add_to_top_left(self, signals):
        self.add_to_possibilities(signals, self.topLeft)

    def add_to_not_top_mask(self, signals):
        self.add_to_possibilities(signals, self.notTop)
    def add_to_not_top_right_mask(self, signals):
        self.add_to_possibilities(signals, self.notTopRight)    
    def add_to_not_center_mask(self, signals):
        self.add_to_possibilities(signals, self.notCenter)
    def add_to_not_bottom_right_mask(self, signals):
        self.add_to_possibilities(signals, self.notBottomRight)
    def add_to_not_bottom_mask(self, signals):
        self.add_to_possibilities(signals, self.notBottom)
    def add_to_not_bottom_left_mask(self, signals):
        self.add_to_possibilities(signals, self.notBottomLeft)
    def add_to_not_top_left_mask(self, signals):
        self.add_to_possibilities(signals, self.notTopLeft)

    def eliminate_possibilities_based_of_mask(self):
        for num in self.top:
            if num in self.notTop:
                self.top.remove(num)
        for num in self.topRight:
            if num in self.notTopRight:
                self.topRight.remove(num)
        for num in self.center:
            if num in self.notCenter:
                self.center.remove(num)
        for num in self.bottomRight:
            if num in self.notBottomRight:
                self.bottomRight.remove(num)
        for num in self.bottom:
            if num in self.bottom:
                self.bottom.remove(num)
        for num in self.bottomLeft:
            if num in self.notBottomLeft:
                self.bottomLeft.remove(num)
        for num in self.topLeft:
            if num in self.notTopLeft:
                self.topLeft.remove(num)

    def decode_number(self, numberSignals: str) -> int:
        if len(numberSignals) == 2:
            return 1
        if len(numberSignals) == 4:
            return 4
        if len(numberSignals) == 3:
            return 7
        if len(numberSignals) == 7:
            return 8

        if KeyValidator.is_signal_matching(self.zeroSignals, numberSignals):
            return 0
        
        if KeyValidator.is_signal_matching(self.twoSignals, numberSignals):
            return 2
        if KeyValidator.is_signal_matching(self.threeSignals, numberSignals):
            return 3
        
        if KeyValidator.is_signal_matching(self.fiveSignals, numberSignals):
            return 5
        if KeyValidator.is_signal_matching(self.sixSignals, numberSignals):
            return 6
        
        if KeyValidator.is_signal_matching(self.nineSignals, numberSignals):
            return 9
        
        return -1

class KeyValidator:
    numberKey: NumberKey
    parodyKeys: list[NumberKey]
    signals: list[str]

    def __init__(self, numKey:NumberKey, signals:list[str]) -> None:
        self.numberKey = numKey
        self.parodyKeys = []
        self.signals = signals
        for top in self.numberKey.top:
            for topLeft in self.numberKey.topLeft:
                for topRight in self.numberKey.topRight:
                    for center in self.numberKey.center:
                        for bottomLeft in self.numberKey.bottomLeft:
                            for bottomRight in self.numberKey.bottomRight:
                                for bottom in self.numberKey.bottom:
                                    if not self.has_duplicates([top, topRight, topLeft, center, bottom, bottomLeft, bottomRight]):
                                        self.parodyKeys.append(NumberKey([top], [topRight], [topLeft], [center], [bottomRight], [bottomLeft], [bottom]))
        print(f"Parody keys initialized ({len(self.parodyKeys)})")

    def has_duplicates(self, input:list[str]) -> bool:
        uniques = list(set(input))
        if len(uniques) == len(input):
            return False
        return True


    def validate_key(self) -> NumberKey:
        valid_combinations = list(filter(lambda key: self.is_valid(key), self.parodyKeys))
        print(f"{len(valid_combinations)} valid keys found")
        self.parodyKeys = valid_combinations
        return valid_combinations[0]

    def is_valid(self, deducedKey: NumberKey) -> bool:
        return self.is_valid_0(deducedKey) and self.is_valid_1(deducedKey) and self.is_valid_2(deducedKey) and self.is_valid_3(deducedKey) and self.is_valid_5(deducedKey) and self.is_valid_6(deducedKey) and self.is_valid_7(deducedKey) and self.is_valid_9(deducedKey)

    @staticmethod
    def is_signal_matching(lettersUsed:list[str], signalCandidate:str):
        for letter in signalCandidate:
            if letter not in lettersUsed:
                # print(f"{letter} not in {lettersUsed} ({signalCandidate})")
                return False

        return True

    def is_valid_0(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.top[0], deducedKey.topRight[0], deducedKey.topLeft[0], deducedKey.bottomRight[0], deducedKey.bottomLeft[0], deducedKey.bottom[0]]
        # length must match
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))

        # letters must match (any order)
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))

        if len(validSignalCandidates) == 1:
            deducedKey.zeroSignals = validSignalCandidates[0]

        return len(validSignalCandidates) > 0

    def is_valid_1(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.topRight[0], deducedKey.bottomRight[0]]
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))
        if len(validSignalCandidates) == 1:
            deducedKey.oneSignals = validSignalCandidates[0]
        return len(validSignalCandidates) > 0

    def is_valid_2(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.top[0], deducedKey.topRight[0], deducedKey.center[0], deducedKey.bottomLeft[0], deducedKey.bottom[0]]
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))
        if len(validSignalCandidates) == 1:
            deducedKey.twoSignals = validSignalCandidates[0]
        return len(validSignalCandidates) > 0

    def is_valid_3(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.top[0], deducedKey.topRight[0], deducedKey.center[0], deducedKey.bottomRight[0], deducedKey.bottom[0]]
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))
        if len(validSignalCandidates) == 1:
            deducedKey.threeSignals = validSignalCandidates[0]
        return len(validSignalCandidates) > 0

    def is_valid_5(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.top[0], deducedKey.topLeft[0], deducedKey.center[0], deducedKey.bottomRight[0], deducedKey.bottom[0]]
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))
        if len(validSignalCandidates) == 1:
            deducedKey.fiveSignals = validSignalCandidates[0]
        return len(validSignalCandidates) > 0

    def is_valid_6(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.top[0], deducedKey.topLeft[0], deducedKey.center[0], deducedKey.bottomRight[0], deducedKey.bottomLeft[0], deducedKey.bottom[0]]
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))
        if len(validSignalCandidates) == 1:
            deducedKey.sixSignals = validSignalCandidates[0]
        return len(validSignalCandidates) > 0

    def is_valid_7(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.top[0], deducedKey.topRight[0], deducedKey.bottomRight[0]]
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))
        if len(validSignalCandidates) == 1:
            deducedKey.sevenSignals = validSignalCandidates[0]
        return len(validSignalCandidates) > 0

    def is_valid_9(self, deducedKey:NumberKey) -> bool:
        lettersUsed = [deducedKey.top[0], deducedKey.topRight[0], deducedKey.topLeft[0], deducedKey.center[0], deducedKey.bottomRight[0], deducedKey.bottom[0]]
        signalCandidates = list(filter(lambda s: len(s) == len(lettersUsed), self.signals))
        validSignalCandidates = list(filter(lambda c : self.is_signal_matching(lettersUsed, c), signalCandidates))
        if len(validSignalCandidates) == 1:
            deducedKey.nineSignals = validSignalCandidates[0]
        return len(validSignalCandidates) > 0
