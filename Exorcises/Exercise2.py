# in this exercise we are goint to ask a number an operation and a second number, show the result and ask for another operation and other number unitl the user input exit


# Result

result = ""

while True:
    if not result:
        result = input("Give me a number: ")
        if result.lower().strip() == "exit":
            break
        result = int(result)
    op = input("operation avaliable = add/ sust/ multi/ div :")
    if op.lower().strip() == "exit":
        break
    num2 = input("Give me another number: ")
    if num2.lower().strip() == "exit":
        break
    num2 = int(num2)

    if op.lower() == "add":
        result += num2
    elif op.lower() == "sust":
        result -= num2
    elif op.lower() == "multi":
        result *= num2
    elif op.lower() == "div":
        result /= num2
    else:
        print("please select an operation: add/ sust/ multi/ div.")
        break

    print(f"Result = {result}")
