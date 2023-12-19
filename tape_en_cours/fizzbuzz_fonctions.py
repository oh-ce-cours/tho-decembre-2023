def est_divisible_par(nombre, modulo):
    return nombre % modulo == 0


def etape_fizz_buzz_1(nombre):
    res = ""
    if est_divisible_par(nombre, 3):
        res = res + "fizz"
    if est_divisible_par(nombre, 5):
        res = res + "buzz"
    if res == "":
        res = str(nombre)
    return res 

def etape_fizz_buzz_2(nombre):
    if est_divisible_par(nombre, 3) and est_divisible_par(nombre, 5):
        return "fizzbuzz"
    elif est_divisible_par(nombre, 3):
        return "fizz"
    elif est_divisible_par(nombre, 5):
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