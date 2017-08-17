# -*- coding: utf-8 -*-
"""El siguente programa."""

# Importamos las librerias necesarias para el uso de ventanas
import wx
import wx.xrc
# Importamos librerias para uso de graficos y arreglos
import numpy as np
import matplotlib.pyplot as plt
# Importamos el diseño del formulario
import form_main


class Principal(form_main.form1):
    """Programa."""

    # Creamos el metodo init de la clase principal
    def __init__(self, parent):
        """Constructor de funcion principal."""
        # Iniciamos la clase superior (El formulario)
        form_main.form1.__init__(self, parent)
        # Declaramos variables de uso global
        self.fila = 8  # Almacenamos el numero de datos iniciales
        self.filaSelec = ""

        # Agregamos columnas a nuestro list control.
        self.ListCtrl.InsertColumn(1, "Desplazamientos", width=245)
        self.ListCtrl.InsertColumn(2, "Fuerza 10⁴N", width=245)

        # Cargamos problema inicial
        self.Despla = [10, 20, 30, 40, 50, 60, 70, 80]
        self.Fuerza = [0.1, 0.17, 0.27, 0.35, 0.39, 0.42, 0.43, 0.44]
        for i in range(0, len(self.Despla)):
            self.ListCtrl.InsertStringItem(i, str(self.Fuerza[i]))
            self.ListCtrl.SetStringItem(i, 1, str(self.Despla[i]))

    def Agregar(self, event):
        """Metodo que agregara los datos ingresados por el usuario."""
        # Agremamos una fila al ListCtrl
        self.ListCtrl.InsertStringItem(self.fila,
                                       str(self.txtDespl.GetValue()))
        # Agregamos los datos a la fila agregada
        self.ListCtrl.SetStringItem(self.fila,
                                    1, str(self.txtFuerza.GetValue()))
        self.fila += 1

        # Limpiamos los TextCtrl
        self.txtDespl.SetValue("")
        self.txtFuerza.SetValue("")
        self.txtDespl.SetFocus()

    def Seleccionar(self, event):
        """Seleciona un elemento de la lista para su eliminacion o edicion."""
        # Obtenemos el indice de la fila seleccionada
        self.filaSelec = self.ListCtrl.GetFocusedItem()
        self.elementoFila = self.ListCtrl.GetItemText(self.filaSelec)

    def Eliminar(self, event):
        """Elimina de la lista el elemento seleccionado."""
        # Comprobamos que se haya seleccionado un elemento
        if self.elementoFila != "":
            self.ListCtrl.DeleteItem(self.filaSelec)
        self.fila -= 1

    def Nuevo(self, event):
        """Vacia todos los campos para ingresar un nuevo problema."""
        self.ListCtrl.DeleteAllItems()  # Limpiamos ListCtrl
        self.txtDespl.SetValue("")      # Limpiamos TextCtrl
        self.txtFuerza.SetValue("")
        self.txtDespl.SetFocus()        # Mandamos el foco a txtDespl
        self.fila = 0                   # Reiniciamos el numero de filas

    def Mostrar(self, event):
        """Metodo que mostrara la grafica de los datos ingresados."""
        self.Obtener_Datos()
        # Convertimos nuestras listas en arreglos
        ArrayDespl = np.array(self.Despla)
        ArrayFuerza = np.array(self.Fuerza)
        # Graficamos nuestros arreglos
        plt.plot(ArrayDespl, ArrayFuerza)
        plt.show()

    def Calcular(self, event):
        """Metodo para calcular la ecuacion lineal y no lineal."""
        self.Obtener_Datos()  # Obtenemos los datos del ListCtrl
        self.DespXFuerz = []  # Lista que almacenara la multiplacion

        # Multiplicamos fuerza por desplazamiento
        for i in range(0, len(self.Despla)):
            self.DespXFuerz.append(round((float(self.Despla[i]) *
                                   float(self.Fuerza[i])), 4))
        self.suma = 0
        # Calculamos la suma de los productos de desplazamiento * fuerza
        for i in self.DespXFuerz:
            self.suma += i

        print self.suma

    def Obtener_Datos(self):
        """"Metodo para pasar los datos del ListCtrl a listas."""
        self.Despla = []
        self.Fuerza = []
        # Agregamos las columnas del ListCtrl en listas
        for i in range(0, self.ListCtrl.GetItemCount()):
            self.Despla.append(self.ListCtrl.GetItemText(i, 0))
            self.Fuerza.append(self.ListCtrl.GetItemText(i, 1))


class MyApp(wx.App):
    """Instanciamos el formulario Principal."""

    def OnInit(self):
        """Metodo que mostrara nuestro formulario en pantalla."""
        frame1 = Principal(None)
        self.SetTopWindow(frame1)
        frame1.Show()
        return 1


# end of class MyApp
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
