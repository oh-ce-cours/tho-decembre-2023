from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# ImportError: dynamic module does not define init function

# I've found that a frequent cause of this problem is,
# when using a distutils setup file to compile the code,
# that the .pyx base name does not match the extension name, e.g:
# ext = Extension(name='different', sources=['cython_ext.pyx']) # Won't work
# To avoid the problem the extension name should be
# exactly the same, in this case, cython_ext.

ext_modules = [
    Extension(
        "test_mview",
        [
            "test_mview.pyx"
        ],
        libraries=["m"],
        extra_compile_args=["-ffast-math", "-fopenmp", "-O3"],
        extra_link_args=["-fopenmp"],
    )
]

setup(
    name="test_mview",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules
)
