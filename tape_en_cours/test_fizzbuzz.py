def est_divisible_par(nombre, modulo):
    return nombre % modulo == 0


# def etape_fizz_buzz_1(nombre):
#     res = ""
#     if est_divisible_par(nombre, 3):
#         res = res + "fizz"
#     if est_divisible_par(nombre, 5):
#         res = res + "buzz"
#     if res == "":
#         res = str(nombre)
#     return res

def etape_fizz_buzz_1(nombre):
    if est_divisible_par(nombre, 5):
        return "buzz"
    elif est_divisible_par(nombre, 3) and est_divisible_par(nombre, 5):
        return "fizzbuzz"
    elif est_divisible_par(nombre, 3):
        return "fizz"
    else:
        return nombre

def test_est_divisible_par():
    assert est_divisible_par(2, 2) == True
    assert est_divisible_par(3, 2) == False
    
    
def test_etape_fizz_buzz_1():
    assert etape_fizz_buzz_1(4) == "4"
    assert etape_fizz_buzz_1(5) == "buzz"
    assert etape_fizz_buzz_1(3) == "fizz"
    assert etape_fizz_buzz_1(15) == "fizzbuzz"
