class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    pass


class Logger2(metaclass=Singleton):
    pass


l1 = Logger()
l1_bis = Logger()
print(l1 is l1_bis)

l2 = Logger2()
print(l1 is l2)
