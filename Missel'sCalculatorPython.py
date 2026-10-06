#Missel Isaac
#COP1000
#Nice calculator is a program where you can easily calculate numbers !

print("Nice Calculator /n V1.0")

#Variables
FirstNumber = int()
SecondNumber = int()
Result = int()
Operation = ""
NoAnswer = "Not a valid sign"

#Input/Ouput
FirstNumber = int(input("Enter the first number"))
Operation = input("Enter the operation sign")
SecondNumber = int(input("Enter the second number"))

#Making calculations
if Operation == "+":
    Result = FirstNumber + SecondNumber
elif Operation == "-":
    Result = FirstNumber - SecondNumber
elif Operation == "*":
    Result = FirstNumber * SecondNumber
elif Operation == "%":
    Result = FirstNumber * SecondNumber
elif Operation == "/":
    Result = FirstNumber / SecondNumber
else:
    print(NoAnswer)

#Final prints statements
print(f"{FirstNumber} {Operation} {SecondNumber} = {Result}")
print("Thank You for using the program!")