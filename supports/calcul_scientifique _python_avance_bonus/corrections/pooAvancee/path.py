#### Separateur non paramétrable
class MyPath:
    def __init__(self, origin):
        self.path = origin

    def __str__(self):
        return str(self.path)

    def __truediv__(self, other):
        new_path = type(self)(self.path + "/" + str(other))
        return new_path


#### Séparateur paramétrable
import abc


class BasePath(abc.ABC):
    def __init__(self, origin):
        self.path = origin

    def __str__(self):
        return str(self.path)

    @abc.abstractmethod
    def get_separator(self):
        pass

    def __truediv__(self, other):
        new_path = type(self)(self.path + self.get_separator() + str(other))
        return new_path


class UnixPath(BasePath):
    def get_separator(self):
        return "/"


class WindowsPath(BasePath):
    def get_separator(self):
        return "\\"
