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

def test_est_divisible_par():
    assert est_divisible_par(2, 2) == True
    assert est_divisible_par(3, 2) == False