
def loadRules(fileName):    
    with open(fileName) as file:
        lines = file.readlines();
        rules = [];
        index = 0
        for line in lines:
            rule = line.strip().split("|");
            rules.append((index, rule[0], rule[1]));
            index += 1;
        return rules;

def loadUpdates(fileName):
    with open(fileName) as file:
        lines = file.readlines();
        updates = [];
        for line in lines:
            update = line.strip().split(",");
            updates.append(update);
        return updates;

def getMiddlePageNumber(update):
    middleIndex = int((len(update) - 1 )/2);
    return int(update[middleIndex]);

def checkRulesOfOneUpdate(rules, update):
    # Keeps track of rules in effect.
    potentialRuleBreaks = [];
    safeRules = [];
    for pageNumber in update:
        for rule in rules:
            if pageNumber == rule[2] and safeRules.count(rule[0]) == 0:
                # The second page number in a rule is present first. If the first one is present later, explode. But for now we're safe...
                potentialRuleBreaks.append(rule[0]);
            # The first page number is present.
            if pageNumber == rule[1]:
                if potentialRuleBreaks.count(rule[0]) > 0:
                    # We found a page out of order, explode.
                    # Since we're interested in the sum of all middle pages, returning 0 will not affect the total result.
                    return 0;
                # If we didn't explode, then the rule is marked as safe for later.
                safeRules.append(rule[0]);
    return getMiddlePageNumber(update);


rules = loadRules("05/input_rules.txt");
updates = loadUpdates("05/input_updates.txt");
#print(rules);
#print(updates);
#print(rules[0][0] == updates[0][1]);

result = 0;
for update in updates:
    current = checkRulesOfOneUpdate(rules, update);
    print(current);
    result += current;

print(result);
