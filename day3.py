#typecasting = The process of converting a value of one data type to another.
             #(string, interger, float, boolean)
             # Explicit vs Implicit



name= "Krishna"
age= 18
gpa= 3.09
student= True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))


# Explicit

gpa = int(gpa)
print(gpa)

age= float(age)
print(type(age))

student = str(student)
print(type(student))


#Implicit

x= 2
y= 2.0

x= x / y

print(x)
