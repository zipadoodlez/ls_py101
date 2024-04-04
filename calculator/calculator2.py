def prompt(message):
    print(f'==> {message}')

def operate():
    operation = input('''==> What operation would you like to perform?
==> 1) Add 2) Subtract 3) Multiply 4) Divide
==> ''')
    match operation:
        case '1':
            prompt(f'{number1} + {number2} = {number1 + number2}')
        case '2':
            prompt(f'{number1} - {number2} = {number1 - number2}')
        case '3':
            prompt(f'{number1} x {number2} = {number1 * number2}')
        case '4':
            prompt(f'{number1} / {number2} = {number1 / number2}')
        case _:
            prompt('Please try again')
            operate()

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

number1 = input("==> What's the first number? ")

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

number1 = int(number1)

number2 = input("==> What's the second number? ")

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

number2 = int(number2)

operate()
