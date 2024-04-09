#START
def stringdc(string):
    return round(float(string), 2)

def dc(number):
    return round(number, 2)

print("Welcome to the car loan calculator!")
#GET principal, apr, duration
def get_principal():
    principal = 0
    while principal <= 0:
        principal = stringdc(input("Please input the total loan amount: "))
    print("principal = ", principal)
    return principal

def get_apr():
    apr = -1
    while apr < 0:
        apr = stringdc(input("Please input the apr: "))
    print("apr = ", apr)
    return apr

def get_duration():
    duration = 0
    while duration <= 0:
        duration = stringdc(
            input("Please input the loan duration in months: ")
        )
    print("duration = ", duration)
    return duration

principal = get_principal()
apr = get_apr()
duration = get_duration()
#CALCULATE monthly interest rate
mir = round((apr / 12)/100, 4)
print("mir = ", mir * 100, "%")
mpp = dc(principal / duration)
print("mpp = ", mpp)
mia = dc(principal * mir)
print("mia = ", dc(mia))

#CALCULATE the first monthly payment using
mp = dc(mpp + mia)
print(f"Your next monthly payment amount is ${mp}")
