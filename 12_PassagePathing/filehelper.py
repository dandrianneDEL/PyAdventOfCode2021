def readfile() -> dict:
    file1 = open('cave.txt', 'r')
    dict = {}
    for line in file1:
        parts = line.split('-')
        p1 = parts[0]
        p2 = parts[1].strip()
        if not p1 in dict.keys():
            dict[p1] = [p2]
        else:
            dict[p1].append(p2)
    return dict