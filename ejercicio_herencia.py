class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return "Color: " + self._color + "\nNro. ruedas: " + str(self._ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.__velocidad = velocidad

    def __str__(self):
        return super().__str__() + "\nVelocidad: " + str(self.__velocidad) + "km/hr"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.__tipo = tipo

    def __str__(self):
        return super().__str__() + "\nTipo: " + str(self.__tipo)

