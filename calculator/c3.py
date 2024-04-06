import json

with open('c3.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def keep_going():

    prompt(data['keepgoing'])
    yn = input()
    if yn == 'y':
        return 1
    if yn == 'n':
        return 0
    print(data['invalidyn'])
    keep_going()


# program starts here

prompt(""" Which language would you like to use today?
           1) english 2) spanish 3) french 4) chinese 5) arabic """)

lang = 0
while lang < 1 or lang > 5:
    lang = int(input())

match lang:
       case 1:
           data = data['en']
       case 2:
           data = data['es']
       case 3:
           data = data['fr']
       case 4:
           data = data['cn']
       case 5:
           data = data['ar']

prompt(data['welcome'])

runprogram = True

while runprogram:

    prompt(data['getfirst'])
    number1 = input()

    while invalid_number(number1):
        prompt(data['invalidnum'])
        number1 = input()

    prompt(data['getsecond'])
    number2 = input()

    while invalid_number(number2):
        prompt(data['invalidnum'])
        number2 = input()

    prompt(data['operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data['invalidop'])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f'The result is {output}')

    runprogram = keep_going()

prompt("Thanks for using the calculator!")
