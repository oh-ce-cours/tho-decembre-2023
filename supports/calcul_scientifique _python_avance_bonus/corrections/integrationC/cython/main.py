from test_mview import hello

## Manipulation strings entre Python et C

a = hello("Matthieu")

print(a)

# Fonctionne avec des unicode aussi
hello("Irène")
hello("💭")

# ATTENTION
# un nom trop long va déclancher une stack overflow
# hello("Matthieu"*232)

# In [3]: hello("a"*31)
# *** stack smashing detected ***: <unknown> terminated
# [1]    5309 abort (core dumped)  ipython





# ==========================================

# Structures

from test_mview import (
    WrapFormation, get_eleves_from_formation,
    get_profs_from_formation, get_nom_prof_from_formation
)

f = WrapFormation(10)
f.random_eleves()
print("nom prof : ", get_nom_prof_from_formation(f))
print("nb eleves : ", get_eleves_from_formation(f))
print("nb profs :", get_profs_from_formation(f))


# ============================================


from test_mview import sum_np_array
import numpy as np
d = np.ones((3, 3))
sum_np_array(d)
