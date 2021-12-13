def read_file():
    # Using readlines()
    file1 = open('signals.txt', 'r')

    signalPairings = []
    for line in file1:
        line = line.strip()
        segments = line.split(" | ")
        
        signals = segments[0].split(" ")
        numbers = segments[1].split(" ")
        signalPairings.append([signals, numbers])
        
    return signalPairings