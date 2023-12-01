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


def palindromo(txt):
    text = txt
    txt = noSpace(txt)
    backwardsTxt = backwards(txt)
    result = txt.lower() == backwardsTxt.lower()
    if result == True:
        print(f"{text} it is a palindrome")
    else:
        print(f"{text} sorry it is not :(")


palindromo("amo la paloma")
palindromo("menem")
palindromo("mi mama me mima")
palindromo("race car")
palindromo("A man a plan a canal  Panama")
