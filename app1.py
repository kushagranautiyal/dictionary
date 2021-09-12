import json
from difflib import get_close_matches

data =json.load(open("076 data.json"))

def pick(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data :
        return data[w.upper()]

    elif len(get_close_matches(w,data.keys()))>0:
        yn =input( "Did you mean %s instead ? Press y for Yes and n for No " % get_close_matches(w,data.keys())[0])
        if yn == "y":
            return data[ get_close_matches(w,data.keys())[0]]
        elif yn == "n":
            return " Sorry we could not find your word  "
        else:
            return " dumb ! read the option correctly "

    else:
        return("the word does not exist!")

word = input("Enter a word : ")

output = pick(word)
if type(output) == list:
    for items in output:
        print (items)
else:
    print(output)
