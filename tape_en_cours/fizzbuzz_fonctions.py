def etape_fizz_buzz_1(nombre):
    res = ""
    if nombre % 3 == 0:
        res = res + "fizz"
    if nombre % 5 == 0:
        res = res + "buzz"
    if res == "":
        res = str(nombre)
    return res 

def fizz_buzz1(debut, fin):
    for nombre in range(debut, fin):
        res = etape_fizz_buzz_1(nombre)
        print(res)
    
def fizz_buzz2(debut, fin):
    for nombre in range(debut, fin):
        if nombre % 3 == 0 and nombre % 5 == 0:
            print("fizzbuzz")
        elif nombre % 3 == 0:
            print("fizz")
        elif nombre % 5 == 0:
            print("buzz")
        else:
            print(nombre)

    
    
fizz_buzz1(1, 101)