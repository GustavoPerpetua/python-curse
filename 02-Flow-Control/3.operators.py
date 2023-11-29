# and, or, not

# if we have a lighter we need :

gas = False
sparkle = True

if gas and sparkle:
    print("you can use the lighter")
# with "and" you need both condition True to turn on the lighter

if gas or sparkle:
    print("you have a lighter")
# with "or" we need only one True condition

if not gas or not sparkle:
    print("you cannot use the lighter")
# we can use not like in this case to change the status from one argumen from True to False and vice versa.

# python with the comparator "and" analize the first argument and if the first argument (left one) is False, is going to stop and not analize the next one.
# But with the comparator "or" if the fisrt one is True, is going to stop and not continue analizing the next ones, if the first one is False is going to continue until finds a True and stop in that one.
