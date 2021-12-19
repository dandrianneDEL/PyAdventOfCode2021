import filehelper
import queue
result = filehelper.readfile()

"""
Validates that a closing character has a matching, expected opening character
if so, returns the queue with the added closingChar
if not, returns none
"""
def validate_queue(q:queue.LifoQueue) -> queue.Queue:
    closedChar = q.get()
    closing_chars_queue = queue.LifoQueue()
    closing_chars_queue.put(closedChar)
    passed_chars = queue.LifoQueue()
    passed_chars.put(closedChar)
    print(f"validating against closed char '{closedChar}'(q = {q.qsize()})")
    
    while(q.qsize() != 0):
        if closing_chars_queue.qsize() == 0:
            break # all closing chars matched an opening char so far
        char = q.get()
        passed_chars.put(char)
        if char in opening_chars:
            lastClosedChar = closing_chars_queue.get()
            print(f"closing_chars_queue.qsize() = {closing_chars_queue.qsize()} after get {lastClosedChar} -> {char}")
            if not is_matching(char, lastClosedChar):
                return None
        else:
            closing_chars_queue.put(char)
    
    #repopulate queue
    while passed_chars.qsize() != 0:
        char = passed_chars.get()
        q.put(char)

    print(f"{q.qsize()} chars validated")
    return q

def is_matching(openingChar, closingChar)->bool:
    isParenthesis = openingChar == '(' and closingChar == ')'
    isBracket = openingChar == '[' and closingChar == ']'
    isBrace = openingChar == '{' and closingChar == '}'
    isCrocodile = openingChar == '<' and closingChar == '>'
    return isParenthesis or isBrace or isBracket or isCrocodile

def score(invalidChar: str) -> int:
    if invalidChar == ')':
        return 3
    if invalidChar == ']':
        return 57
    if invalidChar == '}':
        return 1197
    if invalidChar == '>':
        return 25137

# ******************************************
# PART 1 - Syntax scoring
# Find the first illegal character in each corrupted line of the navigation subsystem. 
# What is the total syntax error score for those errors?
# ******************************************
opening_chars = ['{', '(', '[', '<']
closing_chars = ['}', ')', ']', '>']

total_score = 0
for line in result.corrupted:
    q = queue.LifoQueue()
    index = 0
    isCorrupt = False
    for char in line:
        index += 1
        # if char in opening_chars:
        q.put(char)
        if char in closing_chars:
            validationResult = validate_queue(q)
            if validationResult == None:
                # invalid, add score
                s = score(char)
                print(f"scored {s} for {char}({index}) in {line}")
                total_score += s 
                isCorrupt = True
                break      
            else:
                q = validationResult

    if not isCorrupt:
        result.incomplete.append(line)

print(f"total score: {total_score}")