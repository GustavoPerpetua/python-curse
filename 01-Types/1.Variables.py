# To define a varianle we must do write the next code: variable_name = Value .
# Variables names cannot strart with numbers or contain any spaces.
# When we create variables we are assigning a value in a  memory space,when we call the variable name we will use that memory space and the result will be the saved value.
name = "Gustavo"
print(name)
# if we run this code is going to show us the value of the variable Name in console.
# remember only strings (text) goes with "", the code print("name") is going to show us name in the console. also we can show more than 1 variable with the function print using ","
last_name = "Perpetua"
print(name, last_name)
# we can print also other kind of values like integers (numbers), floats (numbers with .) and booleans (True or False)
age = 29
height = 1.70
married = False
print(name, last_name, age, height, married)

# for variables wirh longs descriptions we must use "x6 (""" """)
description = """ 
Hello, i`m gustavo, Argentinian.i worked as a chef in differents countries, but now im facing the challenge to become a software developer.
"""

print(name, last_name, age, height, married, description)

# To find out the length of our variable we can use the len function like this:

print(len(description))

# This is going to show us the length of the variable description
# Or we can save the data in another variable and then print like this:

length_description = len(description)
print(length_description)

# If we want to access a particular character of our variable we can use [], like this :
print(name[0])

# The index of the first character is 0, also we can acces to the last one with -1.
print(name[-1])

# we can play with this and make things like
print(name[0], "h", name[-1], name[2], name[-4])

# to show more than 2 consecutives values we can use [:], if we left the first or the last argument empty means thar we can from the firts or to the last.
print(name[1:5])
print(name[:4])
print(name[2:])


# we can concatenate 2 variables with +
name_lastName = name + " " + last_name
print(name_lastName)

# the correct way to format a string is with f"{}
fullname = f"{name} {last_name}"
print(fullname)

# if we palt with this we can make things like:

playing = f"{name[:3]} {last_name[0]}{" born in"} {"19" + "94"}"
print(playing)
