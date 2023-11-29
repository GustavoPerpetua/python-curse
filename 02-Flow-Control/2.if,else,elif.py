# The if condition allows a program to execute some statements when a condition is met and others when it is not (else).

age = input("Age please :")
age = int(age)
if 18 <= age < 64:
    print("Welcome to the night club")
elif age > 65:
    print("Too old to go to parties")
else:
    print("You are a minor is not allowed for you")

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
