from decimal import Decimal

def mix(number, secret):
    result = number ^ secret;
    return result;

def prune(secret):
    return secret % 16777216;

def evolutionProcess(givenSecret):
    secret = givenSecret;
    sixtyfour = secret << 6;
    secret = mix(sixtyfour, secret);
    secret = prune(secret);
    thirtytwo = round(secret >> 5);
    secret = mix(thirtytwo, secret);
    secret = prune(secret);
    deumilkarnathuit = secret << 11;
    secret = mix(deumilkarnathuit, secret);
    secret = prune(secret);
    return secret;

def determineFinalSecret(givenSecret, iterations):
    secret = givenSecret;
    for x in range(iterations):
        secret = evolutionProcess(secret);
    return secret;

#print(mix(15,42))
#print(prune(100000000))
#print(1<<6)
#print(34>>5)
#print("Final: " + str(determineFinalSecret(1,2000)));

with open("22/input22.txt") as file:
    lines = file.readlines();
    cumul = 0;
    for line in lines:
        current = determineFinalSecret(int(line), 2000);
        print(current)
        cumul += current;
    print("Total: " + str(cumul));
