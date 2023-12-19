def etape_fizz_buzz_1(nombre):
    res = ""
    if nombre % 3 == 0:
        res = res + "fizz"
    if nombre % 5 == 0:
        res = res + "buzz"
    if res == "":
        res = str(nombre)
    return res 

def etape_fizz_buzz_2(nombre):
    if nombre % 3 == 0 and nombre % 5 == 0:
        return "fizzbuzz"
    elif nombre % 3 == 0:
        return "fizz"
    elif nombre % 5 == 0:
        return "buzz"
    else:
        return nombre


def fizz_buzz1(debut, fin):
    for nombre in range(debut, fin):
        res = etape_fizz_buzz_1(nombre)
        print(res)
    
def fizz_buzz2(debut, fin):
    for nombre in range(debut, fin):
        res = etape_fizz_buzz_2(nombre)
        print(res)

    
    
fizz_buzz1(1, 101)