# we use "for" to iterate (loop through) a list of elements

for number in range(5):
    print("number: ", number)

# It returns a list of items from the selected range
# lets play
x = int(input("Give me a number: "))

for number in range(101):
    print("num: ", number)
    if number == x:
        print("Find it", x)
        break  # stops the cycle when the condition is met
else:
    print("sorry its not a number from 0 to 100")

# like in "if" we use "else" to finish for cicle
