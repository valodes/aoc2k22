# Calcule le business des singes en comptant les deux singes les plus actifs qui inspectent des éléments sur 20 rondes. Multipliez ces nombres ensemble.

import math

with open("./src/day_11/input", "r") as f:
    input = f.readlines()
input = [i.replace("\n", "") for i in input]

# Classe Monkey avec les attributs suivants:
#   - items: La liste des éléments transportés par ce singe. Chaque élément de la liste est le niveau de souci actuel pour cet élément.
#   - operation: Une chaîne pour signifier l'opération sur chaque élément, soit '*' ou '+'
#   - opérande: Une chaîne pour signifier comment appliquer l'opération. Peut être un nombre ou 'ancien'
#   - divTest: Un int à utiliser dans le test de divisibilité.
#   - trueTarget: Si l'élément est divisible par divTest, passez l'élément à ce singe.
#   - FalseTarget: Si l'élément n'est pas divisible par divTest, passez l'élément à ce singe.
class Monkey:
    def __init__(self, items:list, operation:str, operand:str, divTest:int, trueTarget:int, falseTarget:int):
        self.items = items
        self.operation = operation
        self.operand = operand
        self.divTest = divTest
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget

        # Inspection est le nombre total d'éléments inspectés par ce singe.
        self.inspections = 0

    # On itère sur chaque élément et on applique l'opération sur l'élément.
    def perform_operations(self):
        for i in range(len(self.items)):

            if self.operand == 'old':
                operand = self.items[i]
            else:
                operand = int(self.operand)

            if self.operation == '+':
                self.items[i] += operand
            else:
                self.items[i] *= operand

            # Si l'élément est divisible par 3, on le divise par 3.
            self.items[i] = math.floor(self.items[i] / 3)

        # On update le nombre d'inspections de ce singe.
        self.inspections += len(self.items)

    # Retourne le singe vers lequel on doit jeter l'élément.
    def get_target_monkey(self, item):
        if item % self.divTest == 0:
            return self.trueTarget
        return self.falseTarget

    def __str__(self):
        return f"Monkey attributes:\n\tItems: {self.items}\n\tOperation: new = old {self.operation} {self.operand}\n\tTest: Divisible by {self.divTest}\n\tIf true: throw to monkey {self.trueTarget}\n\tIf false: throw to monkey {self.falseTarget}\n\tInspections: {self.inspections}"

# Une liste pour stocker les singes créés.
monkeys = []

# Crée les singes
def initialize_monkeys():
    global monkeys

    for i in range(0, len(input), 7):
        monkey_info = input[i:i+6]
        monkey_info = [m.lstrip() for m in monkey_info]

        # On récupère les éléments du singe et on les convertit en int.
        start_items = monkey_info[1].split(" ")[2:]
        start_items = [s.replace(",", "") for s in start_items]
        start_items = [int(s) for s in start_items]
        
        # On récupère l'opération et l'opérande.
        operation, operand = monkey_info[2].split(" ")[-2:]
        
        # On récupère le divTest et on le convertit en int.
        divTest = monkey_info[3].split(" ")[-1]
        divTest = int(divTest)
        
        # On récupère le target monkey quand division test est True
        trueTarget = monkey_info[4].split(" ")[-1]
        trueTarget = int(trueTarget)

        # On récupère le target monkey quand division test est False
        falseTarget = monkey_info[5].split(" ")[-1]
        falseTarget = int(falseTarget)

        # On crée le singe et on l'ajoute à la liste des singes.
        monkey = Monkey(start_items, operation, operand, divTest, trueTarget, falseTarget)
        monkeys.append(monkey)

# Un round 
def run_single_round():
    global monkeys

    for monkey in monkeys:
        # On récupère le worry level de chaque singe.
        monkey.perform_operations()

        # On jette les éléments du singe vers le bon singe.
        for item in monkey.items:
            target_monkey = monkey.get_target_monkey(item)
            monkeys[target_monkey].items.append(item)

        # Le singe vide sa liste d'éléments.
        monkey.items = []

# On fait 20 rounds
def run_rounds():
    for _ in range(20):
        run_single_round()


# On initialise les singes et on fait 20 rounds.
initialize_monkeys()
run_rounds()

# On récupère les deux singes les plus actifs et on calcule le business des singes.
inspections = [m.inspections for m in monkeys]
inspections.sort()
active_a, active_b = inspections[-2:]
monkey_business = active_a * active_b
print("Monkey business: %d" % monkey_business)