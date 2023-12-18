A = int(input("Entrez un nombre A : "))
B = int(input("Entrez un nombre B : "))

if A == 0 or B == 0:
    print("Il faut que A et B soient non nuls")
else:
    while B != 0:
        if A > B:
            print(A, B)
            A = A - B
        else:
            print(A, B)
            B = B - A
    print(A)
    print("fini")