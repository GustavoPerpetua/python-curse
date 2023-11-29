number = 3  # Integer
decimal = 1.5  # fDecimal numbers are known as FLOATS.
imaginary = 2 + 2j

addition = 5 + 3
sustraction = 8 - 3
multi = 2 * 2
div = 8 / 3
divnofloat = 8//3  # if we dont want float
module = 13 % 5  # give us the remainder
powers = 2**3

print("addition = ", addition)
print("sustaction = ", sustraction)
print("multiplication = ", multi)
print("divition = ", div)
print("No float divition = ", divnofloat)
print("module = ", module)
print("power = ", powers)

# we can make operations with variables
# number = number + 5  === number +=5, same for the other operatios -=, *=, /=

number += 4
print("+result: ", number)
number -= 3
print("-result: ", number)
number *= 3
print("*result: ", number)
number /= 3
print("/result: ", number)

# Time to play

print(number + addition)
print(5 * (sustraction * multi) / 3 * (addition - module))
print(3 * sustraction // div)
print(number + 5 * addition - div)
