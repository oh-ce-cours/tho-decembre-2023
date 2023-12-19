class ConvertisseurTemperature:
    @staticmethod
    def celsius2fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit2celsius(far):
        return (far - 32) * 5/9

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius2fahrenheit(self._celsius)

    @fahrenheit.setter
    def fahrenheit(self, far):
        self._celsius = self.fahrenheit2celsius(far)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, cel):
        self._celsius = cel


def main():
    degres_celsius = 21
    ct = ConvertisseurTemperature(degres_celsius)
    print("initialisation à {}°C".format(degres_celsius))
    print("{}°C -> {}°F".format(ct.celsius, ct.fahrenheit))

    ct.fahrenheit = 0
    print("{}°C -> {}°F".format(ct.celsius, ct.fahrenheit))

    ct.fahrenheit = 32
    print("{}°C -> {}°F".format(ct.celsius, ct.fahrenheit))

    ct.celsius = 34
    print("{}°C -> {}°F".format(ct.celsius, ct.fahrenheit))


if __name__ == '__main__':
    main()