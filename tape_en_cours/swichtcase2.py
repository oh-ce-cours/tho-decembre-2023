lang = "en"

if lang == "fr":
    print("Bonjour")
elif lang == "en":
    print("Hello")
else:
    print("Unsupported language")
    

##################

match lang:
    case "fr":
        print("Bonjour")
    case "en":
        print("Hello")
    case _:
        print("Unsupported language")
