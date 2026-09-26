Math in Python

friends= 10

friends= friends +1 
friends +=1
friends *=3
friends /=2
friends **=2
reminder= friends % 2

print(reminder)


x= 3.14
y= 4
z= 5

result= round(x)
result= abs(y)
result= pow(4,3)
result= max(x, y, z)
result= min(x, y, z)

print(result)

import math

x= 9.9

print(math.pi)
print(math.e)
result= math.sqrt(x)
result= math.ceil()
result= math.floor()

print(result)


import math

radius= float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}")


import math

radius= float(input("Enter the radius of a circle: "))

area= math.pi * pow(radius, 2)

print(f"The area is: {round(area, 2)}")


import math

a= float(input("Enter side A: "))
b= float(input("Enter side B: "))

c= math.sqrt(pow(a, 2)+ pow(b, 2))

print(f"Side C= {c}")