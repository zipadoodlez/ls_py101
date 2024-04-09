#START
def stringdc(string):
    return round(float(string), 2)

def dc(float):
    return round(float, 2)

print("Welcome to the car loan calculator!")
#GET principal, apr, duration

PRINCIPAL = stringdc(input("Please input the total loan amount: "))
APR = stringdc(input("Please input the APR: "))
DURATION = stringdc(input("Please input the loan duration in months: "))

#CALCULATE monthly interest rate 
MIR = dc((APR / 12)/100)
print("MIR = ", MIR * 100, "%")
MPP = dc(PRINCIPAL / DURATION)
print("MPP = ", MPP)
mia = dc(PRINCIPAL * MIR)
print("mia = ", mia)

#CALCULATE the first monthly payment using 
mp = MPP + mia
print(f"Your next monthly payment amount is {mp}")
