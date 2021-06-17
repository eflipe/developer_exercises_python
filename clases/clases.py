'''
Dado un radio, se calcula el área y perímetro de un circulo.
Escribir una clase en python llamada círculo que contenga un radio,
con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción
indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta
setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un
nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0

'''
import math


class Circulo:
    '''
    Dado un radio, se calcula el área y perímetro de un círculo.
    Si el radio es un número menor o igual a cero, devulve un ValueError con un
    mensaje.
    Al multiplar el objeto Circulo por un número, devuelve un nuevo
    objeto con el radio multiplicado por ese número.

    >>> obj_circulo = Circulo(0)
    Traceback (most recent call last):
    ValueError: El valor ingresado no puede ser cero o negativo.
    >>> obj_circulo = Circulo(3)
    >>> obj_circulo.calcular_area()
    28.274333882308138
    >>> obj_circulo.calcular_perimetro()
    18.84955592153876
    >>> obj_circulo_nuevo = obj_circulo * 3
    >>> obj_circulo_nuevo.radio
    9

    '''
    PI = math.pi

    def __init__(self, radio):
        if radio <= 0:
            raise ValueError('El valor ingresado no puede ser cero o negativo.')
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio <= 0:
            raise ValueError('El valor ingresado no puede ser cero o negativo.')
        self._radio = radio

    def calcular_area(self):
        " Devuelve el área del círculo. "
        return Circulo.PI * (self._radio ** 2)

    def calcular_perimetro(self):
        " Devuelve el perímetro del círculo. "
        return 2 * Circulo.PI * self._radio

    def __mul__(self, valor):
        if valor <= 0:
            raise ValueError('El valor ingresado no puede ser cero o negativo.')
        return Circulo(self.radio * valor)

    def __str__(self):
        return f'El objeto Círculo tiene un radio de: {self._radio}.\
                \nSu área es de {self.calcular_area():.4f}. \
                \nSu perímetro es de {self.calcular_perimetro():.4f}.'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
