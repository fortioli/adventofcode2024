pos7 = [0, 3];
pos8 = [1, 3];
pos9 = [2, 3];
pos4 = [0, 2];
pos5 = [1, 2];
pos6 = [2, 2];
pos1 = [0, 1];
pos2 = [1, 1];
pos3 = [2, 1];
posHole = [0, 0];
pos0 = [1, 0];
posA = [2, 0];

posHo = [0,1];
posUp = [1,1];
posA2 = [2,1];
posLe = [0,0];
posDo = [1,0];
posRi = [2,0];

def ugliestBruteForceEver(character):
    match character:
        case "0":
            return pos0;
        case "1":
            return pos1;
        case "2":
            return pos2;
        case "3":
            return pos3;
        case "4":
            return pos4;
        case "5":
            return pos5;
        case "6":
            return pos6;
        case "7":
            return pos7;
        case "8":
            return pos8;
        case "9":
            return pos9;
        case "A":
            return posA;

def secondUgliestBruteForceEver(character):
    match character:
        case "^":
            return posUp;
        case "<":
            return posLe;
        case "v":
            return posDo;
        case ">":
            return posRi;
        case "A":
            return posA2;

def parseFirstCoordinates(code):
    result = [];
    for character in code:
        result.append(ugliestBruteForceEver(character));
    #print("Parsed: " + str(result));
    return result;

def parseArrowCoordinates(code):
    result = [];
    for character in code:
        result.append(secondUgliestBruteForceEver(character));
    #print("Parsed: " + str(result));
    return result;

def movesKeypad(currentPos, position):
    current = currentPos.copy();
    result = [];
    #print("Current: " + str(current) + ", going to: " + str(position))
    while current[0] != position[0] or current[1] != position[1]:
        #print(str(current) + "->" + str(position))
        if current[0] < position [0]:
            current[0] += 1;
            result.append(">");
            if current[0] < position [0]:
                current[0] += 1;
                result.append(">");
            continue;
        # TODO need to check which is better between this
        if current[1] < position [1]:
            current[1] += 1;
            result.append("^");
            if current[1] < position [1]:
                current[1] += 1;
                result.append("^");
            continue;
        # TODO and this
        if current[0] > position [0] and not (current[0] == 1 and current[1] ==  0):
            current[0] -= 1;
            result.append("<");
            if current[0] > position [0] and not (current[0] == 1 and current[1] ==  0):
                current[0] -= 1;
                result.append("<");
                if current[0] > position [0] and not (current[0] == 1 and current[1] ==  0):
                    current[0] -= 1;
                    result.append("<");
            continue;
        if current[1] > position [1] and not (current[0] == 0 and current[1] == 1):
            current[1] -= 1;
            result.append("v");
            if current[1] > position [1] and not (current[0] == 0 and current[1] == 1):
                current[1] -= 1;
                result.append("v");
                if current[1] > position [1] and not (current[0] == 0 and current[1] == 1):
                    current[1] -= 1;
                    result.append("v");
            continue;
    result.append("A");
    #print("Done");
    return result;

def movesArrows(currentPos, position):
    current = currentPos.copy();
    result = [];
    #print("Current: " + str(current) + ", going to: " + str(position))
    while current[0] != position[0] or current[1] != position[1]:
        #print(str(current) + "->" + str(position))
        if current[0] < position [0]:
            current[0] += 1;
            result.append(">");
            if current[0] < position [0]:
                current[0] += 1;
                result.append(">");
            continue;
        if current[1] > position [1]:
            current[1] -= 1;
            result.append("v");
            if current[1] > position [1]:
                current[1] -= 1;
                result.append("v");
            continue;
        if current[1] < position [1] and not (current[0] == 0 and current[1] == 0):
            current[1] += 1;
            result.append("^");
            if current[1] < position [1] and not (current[0] == 0 and current[1] == 0):
                current[1] += 1;
                result.append("^");
            continue;
        if current[0] > position [0] and not (current[0] == 1 and current[1] == 1):
            current[0] -= 1;
            result.append("<");
            if current[0] > position [0] and not (current[0] == 1 and current[1] == 1):
                current[0] -= 1;
                result.append("<");
            continue;
    result.append("A");
    #print("Done");
    return result;

def allInOneString(array):
    result = [];
    for part in array:
        result.append("".join(part));
        #print(result)
    result = "".join(result);
    return result;

def determineFirstRobotMoves(code, current):
    codeCoordinates = parseFirstCoordinates(code);
    result = [];
    for button in codeCoordinates:
        #print("Next in " + str(codeCoordinates) + ": " + str(button));
        result.append(movesKeypad(current, button));
        current = button;
        if (current == posHole):
            print("Dead");
            return [];
    return allInOneString(result);

def determineArrowMoves(code, current):
    codeCoordinates = parseArrowCoordinates(code);
    result = [];
    for button in codeCoordinates:
        #print("Next in " + str(codeCoordinates) + ": " + str(button));
        result.append(movesArrows(current, button));
        current = button;
        if (current == posHo):
            print("Dead");
            return [];
    return allInOneString(result);

def runWhole(code, indirections):
    indirection = determineFirstRobotMoves(code, posA);
    iteration = 0;
    while iteration < indirections:
        indirection = determineArrowMoves(indirection, posA2);
        iteration += 1;
    print(len(indirection));

def runEasy(code):
    return runWhole(code, 2);

#first = determineFirstRobotMoves("379A", posA);
#print(first);
#second = determineArrowMoves(first, posA2);
#print(second);
#third = determineArrowMoves(second, posA2);
#print(third);
#print(len(third));

runEasy("029A");
runEasy("980A");
runEasy("179A");
runEasy("456A");
runEasy("379A");