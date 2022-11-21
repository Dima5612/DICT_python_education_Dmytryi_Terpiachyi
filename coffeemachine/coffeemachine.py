#print('Starting to make a coffee')
#print('Grinding coffee beans')
#print('Boiling water')
#print('Mixing boiled water with crushed coffee beans')
#print('Pouring coffee into the cup')
#print('Pouring some milk into the cup')
#print('Coffee is ready!')
#print("Write how many cups of coffee you will need:")
#number = int(input(">"))
#print("For", number,"cups of coffee you will need:")
#print(number * 200, "ml of water")
#print(number * 50, "ml of milk")
#print(number * 15, "ml of coffee beans")
#need_water = 200
#need_milk = 50
#need_coffee_beans = 15
#water = int(input("Write how many ml of water the coffee machine has:\n>"))
#milk = int(input("Write how many ml of milk the coffee machine has:\n>"))
#coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n>"))
#cups_need = int(input("Write how many cups of coffee will tou need:\n>"))
#cup_coffee = min([water // need_water, milk // need_milk, coffee // need_coffee_beans])
#if cup_coffee == cups_need:
#    print("Yes, I can make that amount of coffee")
#elif cup_coffee > cups_need:
#    print("Yes, I can make that amount of coffee (and even", cup_coffee - cups_need, "morethan that)")
#else:
#    print("No, I can make only", cup_coffee, "cups of coffee")
class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    money = 550
    cups = 9
    status ="wait"
    status = "wait"
    counter = 0
    def __make_coffee(salf, take_money, need_water, need_coffee, need_milk = 0):
        if salf.water < need_water:
            print("Sorry, not enough water!")
        elif salf.coffee < need_coffee:
            print("Sorry, not enough coffee!")
        elif salf.milk < need_milk:
            print("Sorry, not enough milk!")
        elif salf.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            salf.water -= need_water
            salf.coffee -= need_coffee
            salf.milk -= need_milk
            salf.cups -= 1
            salf.money += take_money
    def action(self, command):
        if command == "buy":
            self.status = "make"
        elif command == "fill":
            self.status = "fill"
            self.counter = 0
        elif command == "take":
            print(f"I gave you {self.money}")
            self.money = 0
        elif command == "remaining":
            print("The coffee machine has:")
            print(f"{self.water} of water")
            print(f"{self.milk} of milk")
            print(f"{self.coffee} of coffee")
            print(f"{self.cups} of disposable cups")
            print(f"{self.money} of money")
        elif self.status == "make":
            try:
                type_of_coffee = int(command)
            except:
                type_of_coffee = 4
            if type_of_coffee == 4:
                self.status = "wait"
                return
            elif type_of_coffee == 1:
                self.__make_coffee(4, 250, 16)
            elif type_of_coffee == 2:
                self.__make_coffee(7, 350, 20, 75)
            elif type_of_coffee == 3:
                self.__make_coffee(6, 200, 10, 100)
            self.status = "wait"
        elif self.status == "fill":
            v = int(command)
            if self.counter == 0:
                self.water += v
            elif self.counter == 1:
                self.coffee += v
            elif self.counter == 2:
                self.milk += v
            elif self.counter == 3:
                self.cups += v
                self.status = "wait"
                self.counter = -1
            self.counter += 1
        else:
            self.status = "wait"
coffee_machine = CoffeeMachine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n>")
    coffee_machine.action(action)
    if action == "buy":
        type_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to menu:\n>")
        coffee_machine.action(type_of_coffee)
    elif action == "fill":
        water = input("Write how many ml of water you want to add:\n>")
        coffee_machine.action(water)
        milk = input("Write how many ml of milk you want to add:\n>")
        coffee_machine.action(milk)
        coffee = input("Write how many grams of coffee beans you want to add:\n>")
        coffee_machine.action(coffee)
        cups = input("Write how many disposable coffee cups you want to add:\n>")
        coffee_machine.action(cups)
    elif action == "exit":
        break