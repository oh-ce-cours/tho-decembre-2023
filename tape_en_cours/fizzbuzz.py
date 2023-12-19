for nombre in range(1, 101):
#     res = ""
#     if nombre % 3 == 0:
#         res = res + "fizz"
#     if nombre % 5 == 0:
#         res = res + "buzz"
#     if res == "":
#         res = str(nombre)
#     print(res)        
    divisible_par_5 = nombre % 5 == 0
    divisible_par_3 = nombre % 3 == 0
    
    match divisible_par_3, divisible_par_5:
        case True, True:
            print("fizzbuzz")
        case False, True:
            print("fizzbuzz")

