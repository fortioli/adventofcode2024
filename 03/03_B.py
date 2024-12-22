import re

def multiply(mul):
    mulParts = mul.split(",");
    x = int(mulParts[0].split("(")[1]);
    y = int(mulParts[1].split(")")[0]);
    return x * y;

enabled = True;
DONT = "don't()";
DO = "do()";
MUL = "mul";

with open("03/input.txt") as file:
    lines = file.readlines();
    result = [];
    total = 0;
    for line in lines:
        result = re.findall("((mul[(]\d+,\d+[)])|(do[(][)])|(don't[(][)]))", line);
        for operator in result:
            if DONT in operator:
                enabled = False;
                continue;
            if DO in operator:
                enabled = True;
                continue;
            if (enabled):
                total += multiply(operator[0]);
        #print(DO in result[1][0])
    print(total);
    
