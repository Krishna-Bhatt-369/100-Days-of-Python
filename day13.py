# format specifiers = {value:flags} format a value based on what flags are inserted[cite: 1]

# .(number)f = round to that many decimal places (fixed point)[cite: 1]
# :(number) = allocate that many spaces[cite: 1]
# :03 = allocate and zero pad that many spaces[cite: 1]
# :< = left justify[cite: 1]
# :> = right justify[cite: 1]
# :^ = center align[cite: 1]
# :+ = use a plus sign to indicate positive value[cite: 1]
# := = place sign to leftmost position[cite: 1]
# :  = insert a space before positive numbers[cite: 1]
# :, = comma separator[cite: 1]


price1 = 724673.8374
price2 = 374.943284 
price3 = 74246.38274


#This shows us the decimal place of the number.

print(f"Price 1 is {price1: .2f}")
print(f"Price 2 is {price2: .2f}")
print(f"Price 3 is {price3: .2f}")



#This shows us the space allocated to the numbers.

print(f"Price 1 is {price1: 10}")
print(f"Price 2 is {price2: 10}")
print(f"Price 3 is {price3: 10}")


# :< = left justify[cite: 1]

print(f"Price 1 is {price1: <10}")
print(f"Price 2 is {price2: <10}")
print(f"Price 3 is {price3: <10}")


# :> = right justify[cite: 1]

print(f"Price 1 is {price1: >10}")
print(f"Price 2 is {price2: >10}")
print(f"Price 3 is {price3: >10}")

# :^ = center align[cite: 1]

print(f"Price 1 is {price1: ^10}")
print(f"Price 2 is {price2: ^10}")
print(f"Price 3 is {price3: ^10}")


# :+ = use a plus sign to indicate positive value[cite: 1]


print(f"Price 1 is {price1: +10}")
print(f"Price 2 is {price2: +10}")
print(f"Price 3 is {price3: +10}")


# :  = insert a space before positive numbers[cite: 1]


print(f"Price 1 is {price1: }")
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")


# :, = comma separator[cite: 1]

print(f"Price 1 is {price1: +,.2f }")
print(f"Price 2 is {price2: +,.2f }")
print(f"Price 3 is {price3: +,.2f }")