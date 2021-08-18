import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead ? if yes type Y else N for no: " %get_close_matches(w,data.keys())[0])
        if yn == "Y" :
            return data [get_close_matches(w,data.keys())[0]]
        elif yn == "N" :
            return "Word not found. PLease double check it."
        else:
            return "We didn't understand your query. Please double check it."

    else:
        return "Word not found. PLease double check it."

word=input("Enter word: ")

output=(translate(word))

if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)

