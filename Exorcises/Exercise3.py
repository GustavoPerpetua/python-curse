from pprint import pprint
string = input("give me a string: ")


def noSpace(text):
    return [char for char in text if char != " "]


def charCount(list):
    charsDict = {}
    for char in list:
        if char in charsDict:
            charsDict[char] += 1
        else:
            charsDict[char] = 1
    return charsDict


def order(dict):
    return sorted(dict.items(), key=lambda key: key[1], reverse=True)


def biggest(list):
    max = list[0][1]
    ans = {}
    for order in list:
        if max > order[1]:
            break
        ans[order[0]] = order[1]
    return ans


def createMes(dicc):
    mes = "The ones that are most repeated are: \n"
    for key, value in dicc.items():
        mes += f"- {key.upper()} with {value} reps \n"
    return mes


noSpaceString = noSpace(string)
counts = charCount(noSpaceString)
orderCounts = order(counts)
biggestchars = biggest(orderCounts)
message = createMes(biggestchars)
print(message)
