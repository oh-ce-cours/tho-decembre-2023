from sympy import *


d = expand((a + b + c) ** 12)
print(d)

# pour les plus fous, on peut avoir le résultat directement en 1 ligne
[x for x in str(expand((a + b + c) ** 12)).split(" + ") if "a**3*b**7*c**2" in x]

