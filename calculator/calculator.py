print('Welcome to Calculator!')
# Ask the user for the first number.
number1 = int(input("What's the first number? "))
# Ask the user for the second number.
number2 = int(input("What's the second number? "))
print(f'{number1} {number2}')
# Ask the user for an operation to perform.
operation = -1

def operate():
    global operation
    operation = input('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide\n')
    match operation:
        case '1':
            print(f'{number1} + {number2} = {number1 + number2}')
        case '2':
            print(f'{number1} - {number2} = {number1 - number2}')
        case '3':
            print(f'{number1} x {number2} = {number1 * number2}')
        case '4':
            print(f'{number1} / {number2} = {number1 / number2}')
        case _:
            print('Please try again')
            operate()

operate()
# Perform the operation on the two numbers.
#
