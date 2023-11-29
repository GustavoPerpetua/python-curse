# In this exercise we are going to start making a basic calculator

num1 = input("Please, give me a number: ")
num2 = input("Please, give me a second number: ")

# in this lines we convert the string from the user to a integer number
num1 = int(num1)
num2 = int(num2)

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
