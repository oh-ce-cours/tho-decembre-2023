from inspect import signature, Parameter


class M(type):
    def __new__(cls, name, bases, dict):
        print("in metaclass __new__")
        for n, v in dict.items():
            if callable(v):
                sig = signature(v)
                sig = sig.replace(
                    parameters=[
                        Parameter("self", Parameter.POSITIONAL_ONLY),
                        *sig.parameters.values(),
                    ]
                )
                dict[n] = v
                import ipdb

                ipdb.set_trace()
                print("   * modified : {}".format((n)))

        for n, v in dict.items():
            if callable(v):
                sig = signature(v)
                print("   * check : {}, sig: {}".format(n, sig))

        print("after metaclass")
        return super().__new__(cls, name, bases, dict)


class A(metaclass=M):
    def toto(a, b):
        print("dans toto")
        print(self, a, b)
        print("fin toto")


a = A()
print(A)
import ipdb

ipdb.set_trace()

