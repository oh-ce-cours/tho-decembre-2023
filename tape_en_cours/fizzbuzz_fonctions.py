def fizz_buzz1():
    for nombre in range(1, 101):
        res = ""
        if nombre % 3 == 0:
            res = res + "fizz"
        if nombre % 5 == 0:
            res = res + "buzz"
        if res == "":
            res = str(nombre)
        print(res)
    
def fizz_buzz2():
    for nombre in range(1, 101):
        if nombre % 3 == 0 and nombre % 5 == 0:
            print("fizzbuzz")
        elif nombre % 3 == 0:
            print("fizz")
        elif nombre % 5 == 0:
            print("buzz")
        else:
            print(nombre)

    
    
fizz_buzz1()