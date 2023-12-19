for nombre in range(1, 101):
    res = ""
    if nombre % 3 == 0:
        res = res + "fizz"
    if nombre % 5 == 0:
        res = res + "buzz"
    if nombre % 7 == 0:
        res = res + "bazz"
    if res == "":
        res = str(nombre)
    print(res)        
