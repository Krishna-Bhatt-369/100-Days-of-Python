# if else statemente

age= int(input("Enter your age: "))

if age >=100:
    print("You  are too old to sign up")

elif age >= 18:
    print("You are now signed up!")

else:
    print("You must be 18+ to sign up")


response= input("Would you like food? (Y/N): ")

if response == "Y" :
    print("Have some food")

else:
    print("Ok, Have a good day!")


name = input("Enter your name: ")

if name == "" :
  print("Enter your naem first!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

else:
  print(f"Your name is {name}") 
 
for_sale = True

if for_sale:
    print("This iteam is for sale.")

else:
    print("This item is not for sale. ")
