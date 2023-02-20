formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
commands = ['!help', '!done']

def print_help():
    print('Available formatters: ' + ' '.join(formatters))
    print('Special commands: ' + ' '.join(commands))

user_input = input('Choose a formatter: ')

while user_input != '!done':
    if user_input == '!help':
        print_help()
    elif user_input in formatters:
        print(f'{user_input}')
    else:
        print('Unknown formatting type or command')

    user_input = input('Choose a formatter: ')
