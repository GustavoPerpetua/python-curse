def noSpace(txt):
    new_txt = ""
    for char in txt:
        if char != " ":
            new_txt += char
    return new_txt


def backwards(txt):
    btxt = ""
    for char in txt:
        btxt = char + btxt
    return btxt


def palindrome(txt):
    text = txt
    txt = noSpace(txt)
    backwardsTxt = backwards(txt)
    result = txt.lower() == backwardsTxt.lower()
    if result == True:
        print(f"{text} it is a palindrome")
    else:
        print(f"{text} sorry it is not :(")


palindrome("amo la paloma")
palindrome("menem")
palindrome("mi mama me mima")
palindrome("race car")
palindrome("A man a plan a canal  Panama")
