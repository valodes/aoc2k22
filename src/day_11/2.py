# Ce code calcule l'affaire des singes en comptant les deux singes les plus actifs en inspectant des éléments plus de 10000 tours. 
#Multipliez ces nombres ensemble. Les niveaux de souci ne sont plus divisés par 3.

with open("./src/day_11/input", "r") as f:
    input = f.readlines()
input = [i.replace("\n", "") for i in input]

# Classe du singe avec les attributs suivants:
# - éléments: la liste des éléments transportés par ce singe. Chaque élément de la liste est le niveau de souci actuel pour cet élément.
# - opération: une chaîne pour signifier l'opération sur chaque élément, soit '*' ou '+'
# - opérande: une chaîne pour signifier comment appliquer l'opération. Peut être un nombre ou 'ancien'
# - divTest: un int à utiliser dans le test de divisibilité.
# - trueTarget: si l'élément est divisible par divTest, transmettez l'élément à ce singe.
# - FalseTarget: si l'élément n'est pas divisible par divTest, transmettez l'élément à ce singe.
class Monkey:
    def __init__(self, items:list, operation:str, operand:str, divTest:int, trueTarget:int, falseTarget:int):
        self.items = items
        self.operation = operation
        self.operand = operand
        self.divTest = divTest
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget

        # Inspections est le nombre d'inspections effectuées par ce singe
        self.inspections = 0

    # On effectue les opérations sur chaque élément, mod est le diviseur commun
    def perform_operations(self, divisor:int):
        for i in range(len(self.items)):

            # On récupère l'opérande
            if self.operand == 'old':
                operand = self.items[i]
            else:
                operand = int(self.operand)

            # On effectue l'opération
            if self.operation == '+':
                self.items[i] += operand
            else:
                self.items[i] *= operand

            # On garde les niveaux de souci à la baisse en utilisant le diviseur commun
            self.items[i] %= divisor

        # On met à jour le nombre d'inspections
        self.inspections += len(self.items)

    # On teste la divisibilité d'un élément. Retourne le singe cible.
    def get_target_monkey(self, item):
        if item % self.divTest == 0:
            return self.trueTarget
        return self.falseTarget

    def __str__(self):
        return f"Monkey attributes:\n\tItems: {self.items}\n\tOperation: new = old {self.operation} {self.operand}\n\tTest: Divisible by {self.divTest}\n\tIf true: throw to monkey {self.trueTarget}\n\tIf false: throw to monkey {self.falseTarget}\n\tInspections: {self.inspections}"

# Une liste d'objets Monkey. Le singe à l'index 0 est le singe 0.
monkeys = []

# Diviseur commun parmi tous les diviseurs (les opérandes utilisées dans les tests de division)
commonDiv = 1

# On initialise les singes
def initialize_monkeys():
    global monkeys, commonDiv

    for i in range(0, len(input), 7):
        monkey_info = input[i:i+6]
        monkey_info = [m.lstrip() for m in monkey_info]

        # On récupère les éléments du singe
        start_items = monkey_info[1].split(" ")[2:]
        start_items = [s.replace(",", "") for s in start_items]
        start_items = [int(s) for s in start_items]
        
        # On récupère l'opération et l'opérande
        operation, operand = monkey_info[2].split(" ")[-2:]
        
        # On récupère le diviseur
        divTest = monkey_info[3].split(" ")[-1]
        divTest = int(divTest)
        
        # On récupère les cibles quand le test de division est True
        trueTarget = monkey_info[4].split(" ")[-1]
        trueTarget = int(trueTarget)

        # On récupère les cibles quand le test de division est False
        falseTarget = monkey_info[5].split(" ")[-1]
        falseTarget = int(falseTarget)

        # On crée le singe
        monkey = Monkey(start_items, operation, operand, divTest, trueTarget, falseTarget)
        monkeys.append(monkey)

        # On met à jour le diviseur commun
        commonDiv *= divTest

# On effectue une seule ronde de jeu (on passe les éléments)
def run_single_round():
    global monkeys, commonDiv

    # Pour chaque singe
    for monkey in monkeys:
        # On effectue les opérations sur les éléments
        monkey.perform_operations(commonDiv)

        # On transmet les éléments aux singes cibles
        for item in monkey.items:
            target_monkey = monkey.get_target_monkey(item)
            monkeys[target_monkey].items.append(item)

        # On vide la liste des éléments du singe
        monkey.items = []

# On effectue 10000 rondes de jeu
def run_rounds():
    for _ in range(10000):
        run_single_round()


# On initialise les singes et on effectue les 10000 rondes de jeu
initialize_monkeys()
run_rounds()

# On récupère les deux singes les plus actifs et on calcule le nombre d'éléments transportés par ces deux singes
inspections = [m.inspections for m in monkeys]
inspections.sort()
active_a, active_b = inspections[-2:]
monkey_business = active_a * active_b
print("Monkey business: %d" % monkey_business)