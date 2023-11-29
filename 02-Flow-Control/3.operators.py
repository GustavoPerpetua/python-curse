# and, or, not

# if we have a lighter we need :

gas = False
sparkle = True

if gas and sparkle:
    print("you can use the lighter")
# with and you need both condition True to turn on the lighter

if gas or sparkle:
    print("you have a lighter")

if not gas or not sparkle:
    print("you cannot use the lighter")
