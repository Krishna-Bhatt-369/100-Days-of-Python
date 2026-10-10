#Loops and Nested loops make up for 2 days. I got a bit busy so I was unable to do it so I will do these today and try to cover all the topics for 2 days ty.


#Loops

print("Hello")
print("Hello")
print("Hello")
print("Hello")

#This usually takes time to print Hello for 100 or 200 times. So we use loops to make it easier and simpler.

for i in range(4):
    print("Hello")  # It simply told the computer to print Hello 4 times rather taht typong same thing for 4 times soo it makes work easier.


#for

# Tells Python to repeat something for each item in a sequence.

# i
# A variable that takes a different value during each repetition. You can name it something else, too.

# range(5)
# Generates the numbers 0, 1, 2, 3, 4 — five numbers, starting from zero.

# print("Hello")
# Runs once for every value in the range. Notice the indentation!
 

#Lets look how i works.

for i in range(5):
    print(i)    #It should print 0, 1, 2, 3, 4.




#range(start, stop)
for i in range(1,6):
    print(i)   # It will print 1,2,3,4,5. It starts from 1 and goes till 6 but it will not include 6. It will stop at 5.


#range(start, stop, step)

for i in range(1, 10, 9):
    print(i)   # It will print 1, 10 is not included. It will start from 1 and go till 10 but it will not include 10. It will stop at 9. The step is 9 so it will add 9 to the previous number and print the next number which is 10 but it will not include it. So it will stop at 1.



#Reversed loops

for x in reversed(range(1, 11)):
    print(x)    #It will print this numbers backwards.



#skip a number in a loop.


for x in range(1, 70):
    if x == 69:
        continue
    else:
     print(x)   #This will skip 69 and print all the remaining numbers.



#Breaking out of a loop. :)

for x in range(1, 70):
    if x == 5:
         break
    else:
     print(x)   #This won't show the numbers after 5.



#What is nested loop?

#Nested loop are simply loops inside loops(outer, inner).

#          outer loop:
                    #inner loop:





for x in range(4):

 for y in range(1, 10):

    print(y, end= " ") #This will print in same line.
    print()  #This will print everyting in next line.



rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):

 for y in range(columns):

    print(symbol, end= " ") #This will print in same line.
    print()  #This will print everyting in next line.

