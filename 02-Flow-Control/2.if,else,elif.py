# The if condition allows a program to execute some statements when a condition is met and others when it is not (else).

age = input("Age please :")
age = int(age)
if 65 <= age:
    print("sorry, you are too old for this stablishment")
elif 18 < age < 65:
    print("Welcome to the night club")
else:
    print("too young, go home")
# Only if the previous condition is false will the following be evaluated, first if then elif and last else, from te top to the bottom of the code.

# Ternary

# if age > 18:
#     message ="old enough"
# else:
#     message = "too young"
# print(message)


# We can compress the code in only one line using a Ternary like this:

message = "old enough" if age > 18 else "Too young"
print(message)

# we can use ternary when you have only one condition

# lets play

if 18 < age < 30:
    print("what are you going to drink")
elif 30 <= age < 50:
    print("you have a bonus 30% discont on drinks ")
elif 50 <= age < 65:
    print("Hi sir, thank ypu for coming we have a special promotion 2x1 in champagne")
else:
    print("Sorry, but i think you dont supose to be here")
