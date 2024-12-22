first_list = [];
second_list = [];
counts = {};

def getDistance(a, b):
    if a < b:
        return abs(b-a);
    return abs(a-b);

with open("input.txt") as file:
    lines = file.readlines();
    lineNumber = 0;
    for line in lines:
        lineValues = line.split("   ");
        first_list.append(int(lineValues[0]));
        second_list.append(int(lineValues[1]));
        lineNumber+=1;
    #first_list.sort();
    #second_list.sort();
    total = 0;
    for pippo in range(lineNumber):
        tizio = first_list[pippo];
        tizioCount = counts.get(tizio);
        if (tizioCount == None):
            tizioCount = second_list.count(tizio)
            print(first_list);
            print(second_list);
            counts[tizio] = tizioCount;
            print("Value " + str(tizio) + " appears " + str(tizioCount) + " times in the list.");
        print(counts);
        total += tizio * counts.get(tizio);
    print(total)
