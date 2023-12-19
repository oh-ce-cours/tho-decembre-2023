from libc.stdlib cimport calloc, free
from libc.stdlib cimport rand, RAND_MAX

cdef extern from "array_manip.c":
    void format_hello(char* res, char* name)

    ###################

    ctypedef struct Formation:
        # on ne met que les champs d'interet
        int nb_eleves

    int get_nb_eleves(Formation* f)
    int get_nb_profs(Formation* f)
    void get_nom_prof(Formation *f, char* buf)

    ###################

    double somme_elements(double *A, int m, int n)


##################################################################


cpdef str hello(str name):
    """Les chaines de charactères doivent etre "nettoyées" entre le C et python.

    https://stackoverflow.com/questions/30531819/how-to-create-empty-char-arrays-in-cython-without-loops/30553319
    http://docs.cython.org/en/latest/src/tutorial/strings.html
    """
    cdef char res[40]
    res[:6] = "Hello "

    # protection stack overflow
    if len(name) > 40 - 6 - 1:
        raise MemoryError

    byte_name = name.encode()
    cdef char* c_name = byte_name
    format_hello(res, c_name)
    cdef bytes py_string = res

    return py_string.decode().strip()


##################################################################

cdef class WrapFormation:
    cdef Formation* s

    def __cinit__(self, int nb_eleves):
        self.s = create_formation(nb_eleves)

    def __dealloc__(self):
        free(<void *>self.s)

    def double_eleves(self):
        self.s.nb_eleves = self.s.nb_eleves * 2

    def random_eleves(self):
        nb = 1 + int(rand() % 100)
        self.s.nb_eleves = nb


cdef Formation* create_formation(int nb_eleves):
    cdef Formation* p_f = <Formation *>calloc(1, sizeof(Formation))
    p_f.nb_eleves = nb_eleves
    return p_f


cpdef int get_eleves_from_formation(WrapFormation f):
    return get_nb_eleves(f.s)


cpdef int get_profs_from_formation(WrapFormation f):
    return get_nb_profs(f.s)

cpdef str get_nom_prof_from_formation(WrapFormation f):
    cdef char nom[120]
    get_nom_prof(f.s, nom)
    return (<bytes> nom).decode()

##################################################################

cimport numpy as np


cpdef double sum_np_array(np.ndarray[double, ndim=2, mode="c"] np_array):
    cdef int m, n

    m, n = np_array.shape[0], np_array.shape[1]

    return somme_elements(
        <double*> np_array.data,
        m, n
    )