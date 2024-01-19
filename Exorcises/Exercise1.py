# In this exercise we are going to start making a basic calculator, needs to add, sust, mult and div, two numbers

num1 = int(input("Please, give me a number: "))
num2 = int(input("Please, give me a second number: "))
# in this lines we convert the string from the user to a integer number

# Result

add = num1 + num2
sust = num1 - num2
multi = num1 * num2
div = num1 / num2

messaage = f"""
Results of the numbers {num1} & {num2}
adding = {add}
sustraction = {sust}
multiplication = {multi}
divition =  {div}
"""
print(messaage)
