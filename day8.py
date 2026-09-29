#simple calculator

operator= input("Enter an operator (+,-,*,/):")
num1=float(input("Enter input First number:"))
num2=float(input("Enter input Second number:"))

if operator == "+":
    print("Your number is:", round(num1+num2, 3))

elif  operator == "-":
    print("Your number is:", round(num1-num2, 3))

elif  operator == "*":
    print("Your number is:", round(num1*num2, 3))


elif operator == "/":
    print("Your number is:", round(num1/num2, 3))


else:
    print(f"{operator} is invalid.")



#Today, I made a simple calculator using Python Operators.







