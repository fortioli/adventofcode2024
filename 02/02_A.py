
def isConsistent(preprevious, previous, current):
    #print("Start isConsistent")
    # No change: always bad.
    if (previous == current):
        print ("********* Unsafe! Levels jammed!");
        return False;
    # Determine direction.
    preascending = preprevious - previous;
    ascending = previous - current;

    print ("Ascending order is " + str(preascending < 0) + str(ascending < 0));
    if ((preascending < 0 and ascending < 0) or (preascending > 0 and ascending > 0)):
        print ("Safe: levels consistent...");
        return True;
    print ("********* Unsafe! Levels inconsistent!");
    return False;

def isSafeJump (previous, current):
    #print("Start isSafeJump")
    if (abs(previous-current) > 3):
        print ("********* Unsafe! Jump too high!");
        return False;
    #print ("Safe: jump is between parameters...");
    return True;

def fillLevelsWithInt(report):
    #print("Start fillLevelsWithInt")
    splitReport = report.split(" ");
    levels = [];
    for level in splitReport:
        levels.append(int(level));
    #print(levels);
    return levels;

def isSafe(report):
    #print("Start isSafe")
    levels = fillLevelsWithInt(report);
    prepreviousLevel = -1;
    previousLevel = -1;
    for level in levels:
        print("Currently checking these levels: " + str(prepreviousLevel) + "->" + str(previousLevel) + "->" + str(level));
        if(prepreviousLevel < 0):
            #print("Preprevious level not set yet.");
            prepreviousLevel = level;
            continue;
        if(previousLevel > 0):
            if (isSafeJump(previousLevel, level) 
                and isConsistent(prepreviousLevel, previousLevel, level)):
                print("Levels are safe A: " + str(previousLevel) + "->" + str(level));
                previousLevel = level;
                continue;
            return False;
        #print("Previous level not set yet.");
        previousLevel = level;
        if (isSafeJump(prepreviousLevel, previousLevel)):
            print("Levels are safe B: " + str(prepreviousLevel) + "->" + str(previousLevel));
            continue;
        return False;
    print(">>>>>>>>>>>>> Report is safe: " + str(levels));
    return True;
        
def printsomestuff(a):
    print("This is a: " + a);

with open("02/input.txt") as file:
    #printsomestuff("Test");
    lines = file.readlines();
    totalSafe = 0;
    for report in lines:
        if (isSafe(report)):
            totalSafe+=1;
    print(totalSafe);