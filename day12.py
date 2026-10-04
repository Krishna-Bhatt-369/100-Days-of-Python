#string indexing= how we refer to individual char in a string. 
# [ start : end : step ]


credit_number= "1234-4123-4534-534"

print(credit_number[0])
# print(credit_number[0:5])
print(credit_number[:5]) #Both woorks as same.
print(credit_number[5:9])
print(credit_number[5:]) 
print(credit_number[-1]) #prints last character
print(credit_number[::2]) #prints every second character

last_digits = credit_number[-4: ]
print(f"XXXX-XXXX-XXXX-{last_digits}")





#I just get the thing now why phython coder always says you are my [0] priority. :)



