import re

def multiply(mul):
    mulParts = mul.split(",");
    x = int(mulParts[0].split("(")[1]);
    y = int(mulParts[1].split(")")[0]);
    return x * y;

with open("03/input.txt") as file:
    lines = file.readlines();
    result = [];
    total = 0;
    for line in lines:
        result = re.findall("mul[(]\d+,\d+[)]", line);
        for mul in result:
            total += multiply(mul);
    print(total);
