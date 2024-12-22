
def fillMachines():
    machines = [];
    with open("13/test_input.txt") as file:
        lines = file.readlines();
        # Init at -1 to start at 0;
        machineNumber = -1;
        print(len(lines));
        for i in range(len(lines)):
            if (i%4 == 0):
                machineNumber+=1;
                machines.append([])
            if(i%4 != 3):    
                machines[machineNumber].append(lines[i].strip());
        return machines;

machines = fillMachines();

# Extract useful machine info
buttonA = machines[0][0].split(':')[1].split(',');
buttonA[0] = int(buttonA[0].split('+')[1]);
buttonA[1] = int(buttonA[1].split('+')[1]);
buttonB = machines[0][1].split(':')[1].split(',');
buttonB[0] = int(buttonB[0].split('+')[1]);
buttonB[1] = int(buttonB[1].split('+')[1]);
prize = machines[0][2].split(':')[1].split(',');
prize[0] = int(prize[0].split('=')[1]);
prize[1] = int(prize[1].split('=')[1]);

print(buttonA)
print(buttonB)
print(prize)

# a = (8400 - 22 * b) / 94
# a = (5400 - 67 * b) / 34
# (8400 - 22 * b) / 94 = (5400 - 67 * b) / 34
# -22 * b * 34 = (5400 - 67 * b - 8400) * 94
# -22 * 34 * b + 67 * 94 * b = (5400 - 8400) * 94
# b = (P[1] - P[0]) * A[0] / (-B[0] * A[1] + B[1] * A[0])
# b = 
# a = (P[0] - B[0] * b) / A[0]