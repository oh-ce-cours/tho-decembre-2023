# Compile Cython extension 

## Dependancies

### problem 

```
test_mview.c:527:10: fatal error: numpy/arrayobject.h: Aucun fichier ou dossier de ce type
 #include "numpy/arrayobject.h"
```

### solution
sudo apt install python3-numpy-dbg


## compilation

python setup.py build_ext --inplace

# Use 

```
python main.py                     
# Hello Matthieu !
# nom prof :  
# nb eleves :  84
# nb profs : 0
```