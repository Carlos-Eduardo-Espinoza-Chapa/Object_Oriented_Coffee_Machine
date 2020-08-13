import sys


class CoffeeMachine:
    machine_state = {}
    drinks = {}

    def __init__(self):
        self.machine_state = {
            "water": 400,
            "milk": 540,
            "coffee beans": 120,
            "disposable_cups": 9,
            "money": 550
        }
        self.drinks = {1: {"name": "espresso", "water": 250, "milk": 0, "coffee beans": 16, "price": 4},
                       2: {"name": "latte", "water": 350, "milk": 75, "coffee beans": 20, "price": 7},
                       3: {"name": "cappuccino", "water": 200, "milk": 100, "coffee beans": 12, "price": 6}}


    def remaining(self):
        print("The coffee machine has:")
        for key, value in self.machine_state.items():
            if key != "money":
                print("{} of {}".format(value, key))
            elif key == "money":
                print("${} of {}".format(value, key))
        self.choose()


    def buy(self):
        obj = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if obj == "back":
            return self.choose()
        for key, value in self.machine_state.items():
            i = value
            if key != "money" and key != "disposable_cups":
                i -= self.drinks[int(obj)][key]
                if i < 0:
                    print("Sorry, not enough {}!".format(key))
                    return self.choose()
        print("I have enough resources, making you a coffee!")

        self.machine_state["water"] -= self.drinks[int(obj)]["water"]
        self.machine_state["milk"] -= self.drinks[int(obj)]["milk"]
        self.machine_state["coffee beans"] -= self.drinks[int(obj)]["coffee beans"]
        self.machine_state["disposable_cups"] -= 1
        self.machine_state["money"] += self.drinks[int(obj)]["price"]
        self.choose()


    def fill(self):
        self.machine_state["water"] += int(input("Write how many ml of water do you want to add:"))
        self.machine_state["milk"] += int(input("Write how many ml of milk do you want to add:"))
        self.machine_state["coffee beans"] += int(input("Write how many grams of coffee beans do you want to add:"))
        self.machine_state["disposable_cups"] += int(input("Write how many disposable cups of coffee do you want to add:"))
        self.choose()


    def take(self):
        out = self.machine_state["money"]
        self.machine_state["money"] -= out
        print("I gave you ${}".format(out))
        self.choose()


    def exit(self):
        sys.exit(0)


    def choose(self):
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()
        else:
            self.exit()


coffee_instance = CoffeeMachine()
coffee_instance.choose()
