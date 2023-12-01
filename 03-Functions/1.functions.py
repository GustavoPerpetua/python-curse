# to create a function we need to use :

def nameFunction():
    # everything we want to do with our function has to be identified inside our function.
    print("this is our first function")


nameFunction()
# remermber to call the function with ()


def hello(parameter):
    print(f"Hello {parameter}, how are you?")
    print(f"Welcome")


hello("Argument")


def hi(parameter, parameter2="option"):
    print(f"hi {parameter} {parameter2}")


hi("arguemnt", "2nd argument")
hi("argument")  # when we asign a parameter is optional to insert a second argument


def add(*numbers):  # if we named an parameter with * allowes us to insert multiple arguments
    result = 0
    for number in numbers:
        result += number
    print(f" adding results: {result}")


add(1, 3, 4, 5, 6)
