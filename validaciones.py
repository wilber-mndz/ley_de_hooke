# -*- coding: utf-8 -*-
"""Archivo que contiene las validaciones del programa."""


class Validaciones():
    """Clase principal que contiene los metodos para validar datos."""

    def __init__(self):
        """Constructor de la clase validar."""
        # Declarando variables de uso global
        self.elementoFila  # Almacena el indice del elemento seleccionado

    def Validar_Float(self, numero):
        """Verifica que el usuario solo ingrese numeros de tipo float."""
        numFloat = str(numero)
        lon = len(str(numFloat))
        # Si el usuario engresa caracteres que no sean numeros los eliminamos
        if numFloat != '':
            if str(numFloat)[lon-1:] != '.' or str(numFloat)[lon - 2:] == '..':
                try:
                    numFloat = int(numFloat)
                except ValueError:
                    try:
                        # Verificamos que haya ingresado numeros
                        numFloat = float(numFloat)
                    except ValueError:
                        # Si ingreso otro tipo de valor lo eliminamos
                        numFloat = str(numFloat)[:lon - 1]

        # Si el usuario ingreso un dato invalido se devuelve el valor corregido
        if str(numFloat) != str(numero):
            return numFloat
        else:
            # Si no se devuelve el mismo valor
            return numero
