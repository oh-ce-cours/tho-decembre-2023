from ctypes import (
    CDLL, c_char_p,
    create_string_buffer, c_int
)

SIZE = 40

def main_factorielle():
    lib_factorielle = CDLL('./libtest2.so')
    factorielle = lib_factorielle.factorielle

    for i in range(10):
        print("factorielle {} : {}".format(
            i, factorielle(i))
        )

def main_hello():
    lib_hello = CDLL('./libtest1.so')

    res = create_string_buffer(SIZE)

    format_hello = lib_hello.format_hello
    format_hello.argtypes = [c_char_p, c_char_p, c_int]

    name = "Matthieu" * 202
    format_hello(res, name.encode(), SIZE - 1)

    print(res.value)
    print(res.raw)

if __name__ == '__main__':
    main_hello()
    main_factorielle()
