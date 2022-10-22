number =int(input("Enter the number of friends joining (including you):\n>"))
print(number)
if number <= 0:
    print('No one is joining for the party.')
    exit ()
Debtors = {}
print('Enter the name of every friend (including you), each on a new line:')
for _ in range(number):
    name = input(">")
    Debtors[name] = 0
print(Debtors)