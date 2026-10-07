#while loops in python.

name = input("Enter your name: ")

# if name == "":
#     print("You did not enter a name.")
# else:
#     print(f"Hello {name}")


name = input("Enter your name: ")

while name == "":
    print("You did not enter a name.")
    name = input("Enter your name: ") #If we wont put this here it will bwcomw an infinite loop.
    
print(f"Hello {name}")


age = input("Enter your age: ")
age = int(age)

while age < 0:
    print("Age cant be negative.")
    age = int(input("Enter your age: ")) #If we wont put this here it will bwcomw an infinite loop.
    
print(f"Hello, Your age is {age} years old.")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("Bye")



num = int(input("Enter a number between 1 to 10:"))

while num <1 or num > 10:
    print("Number is out of range.")
    num = int(input("Enter a number between 1 to 10:"))
