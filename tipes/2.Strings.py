# We can use different methods for strings

dish = "  riccota Ravioli  "
print("Upper :", dish.upper())
print("lower :", dish.lower())
print("strip :", dish.strip())
print("left strip :", dish.lstrip())
print("right strip :", dish.rstrip())
print("Capilalize :", dish.strip().capitalize())
print("Title :", dish.title())
print(dish.find("ta"))  # retutn index of character, if doesnt exist returns -1
# we can use te function print to know if some characters are in the varible.
print("ricc" in dish)
print("ricc" not in dish)
print("replace :", dish.replace("ta", "lime"))  # first argument x second
