number =int(input("Enter the number of friends joining (including you):\n>"))
if number <= 0:
    print('No one is joining for the party.')
    exit ()
Debtors = {}
print('Enter the name of every friend (including you), each on a new line:')
for _ in range(number):
    name = input("-")
    Debtors[name] = 0
duty = int(input('Enter the total amount:\n>'))
a = round(duty/number, 2)
for name in Debtors:
    Debtors[name] = a
print(Debtors)