class TestMetaclass(type):
    def __new__(cls, clsname, bases, dct):
        print("__new__ dans la metaclasse")
        return super(TestMetaclass, cls).__new__(cls, clsname, bases, dct)

    def __call__(cls, *args, **kwargs):
        print("__call__ dans la metaclasse")
        return super().__call__()


class Test(metaclass=TestMetaclass):
    def __new__(typ, *args, **kwargs):
        print("__new__ dans la classe")
        return super().__new__(typ, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__ dans l'instance")


print("instantiation de Test")
print("Test()")
t = Test()
print("t()")
t()
