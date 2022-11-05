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
water = 400
milk = 540
cups = 9
coffee_beans = 120
money = 550
print("The coffee machine has: ")
print(water, "of water")
print(milk, "of milk")
print(coffee_beans, "of coffee beans")
print(cups, "disposable cups")
print(money, " of money")
action = input("Write action (buy, fill, take):\n>")
if action == "buy":
    species_of_coffee= int(input("What do you want to buy? 1-espresso, 2-latte, 3-cappuccino:\n>"))
    if species_of_coffee == 1:
        if water >= 250 and coffee_beans >= 16 and cups >= 1:
            water -= 250
            coffee_beans -= 16
            cups -= 1
            money += 4
        elif species_of_coffee == 2:
            if water >= 350 and milk >= 75 and cups >= 1 and coffee_beans >= 20 :
                water -= 350
                milk -= 75
                coffee_beans -= 20
                cups -= 1
                money += 7
        elif species_of_coffee == 3:
            if water >= 200 and milk >= 100 and coffee_beans >= 12 and cups >= 1:
                water -= 200
                milk -= 100
                cups -= 1
                money += 6
elif action == "fill":
    water += int(input("Write how many ml of water you want to add:\n>"))
    milk += int(input("Write how many ml of milk you want to add:\n>"))
    coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n>"))
    cups += int(input("Write how many disposable coffee cups you want to add:\n>"))
elif action == "take":
    print(f"I gave you {money} ")
    money = 0
print("The coffee machine has: ")
print(water, " of water")
print(milk, " of milk")
print(coffee_beans, " of coffee beans")
print(cups, "disposable cups")
print(money, " of money")
