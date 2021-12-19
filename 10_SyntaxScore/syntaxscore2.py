import filehelper
import queue
result = filehelper.readfile()

opening_chars = ['{', '(', '[', '<']
closing_chars = ['}', ')', ']', '>']
closing_dict = {'{':'}', '(':')', '[':']', '<':'>'}
closing_score_dict = {')':1, ']':2, '}':3, '>':4}

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
    
    while(q.qsize() != 0):
        if closing_chars_queue.qsize() == 0:
            break # all closing chars matched an opening char so far
        char = q.get()
        passed_chars.put(char)
        if char in opening_chars:
            lastClosedChar = closing_chars_queue.get()
            if not is_matching(char, lastClosedChar):
                return None
        else:
            closing_chars_queue.put(char)
    
    #repopulate queue
    while passed_chars.qsize() != 0:
        char = passed_chars.get()
        q.put(char)

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

def determine_incomplete(lines):
    incompletes = []
    for line in lines:
        q = queue.LifoQueue()
        isCorrupt = False
        for char in line:
            q.put(char)
            if char in closing_chars:
                validationResult = validate_queue(q)
                if validationResult == None:
                    isCorrupt = True
                    break      
                else:
                    q = validationResult

        if not isCorrupt:
            incompletes.append(line)
    return incompletes

def get_correction_string(line:str)->list[str]:
    closing_chars_to_append = []
    opening_char_stack = []
    for char in line:
        if char in opening_chars:
            opening_char_stack.append(char)
        else:
            openingCharToClose = opening_char_stack.pop()
            if not is_matching(openingCharToClose, char):
                closing_chars_to_append.append(closing_dict[openingCharToClose])

    for unclosedChar in opening_char_stack:
        closing_chars_to_append.append(closing_dict[unclosedChar])

    closing_chars_to_append.reverse()
    return ''.join(closing_chars_to_append)

def score_correction(correctionStr:list[str])->int:
    score = 0
    for char in correctionStr:
        score *= 5
        score += closing_score_dict[char]
    return score

# ******************************************
# PART 2 - Syntax scoring corrupted lines
# Find the completion string for each incomplete line, score the completion strings, and sort the scores. 
# What is the middle score?
# ******************************************
scores = []
incompletes = determine_incomplete(result.corrupted)
for line in incompletes:
    correctionStr = get_correction_string(line)
    score = score_correction(correctionStr)
    print(f"scored {score} for {correctionStr} in {line}")
    scores.append(score)

scores.sort()
medianIndex = int(len(scores)/2)
midscore = scores[medianIndex]
print(f"mid score: {midscore}")