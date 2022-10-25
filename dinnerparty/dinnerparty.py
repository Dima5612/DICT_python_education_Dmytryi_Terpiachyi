import random
yes_or_no = {'yes': True, 'no': False}
number = int(input("Enter the number of friends joining (including you):\n>"))
if number <= 0:
    print('No one is joining for the party.')
    exit()
Debtors = {}
print('Enter the name of every friend (including you), each on a new line:')
for _ in range(number):
    name = input("-")
    Debtors[name] = 0
duty = int(input('Enter the total amount:\n>'))
print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
lucky = yes_or_no[input("-").lower()]
lucky_name = ''
if lucky:
    lucky_name = random.choice(list(Debtors.keys()))
    print(lucky_name, "is the lucky one!")
else:
    print("No one is going to be lucky")
all_duty = round(duty/(number - int(lucky)), 2)
for q in Debtors.keys():
    Debtors[q] = all_duty
if lucky:
    Debtors[lucky_name] = 0
print(Debtors)
