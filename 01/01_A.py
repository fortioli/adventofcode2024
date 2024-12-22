first_list = [];
second_list = [];
distances = [];

def getDistance(a, b):
    if a < b:
        return abs(b-a);
    return abs(b-a);

with open("input.txt") as file:
    lines = file.readlines();
    lineNumber = 0;
    for line in lines:
        lineValues = line.split("   ");
        first_list.append(lineValues[0]);
        second_list.append(lineValues[1]);
        lineNumber+=1;
    first_list.sort();
    second_list.sort();
    total = 0;
    for pippo in range(lineNumber):
        total += getDistance(int(first_list[pippo]), int(second_list[pippo]));
    print(total)
