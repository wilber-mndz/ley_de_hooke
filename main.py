# -*- coding: utf-8 -*-
"""El siguente programa."""

# Importamos las librerias necesarias para el uso de ventanas
import wx
import wx.xrc
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
        self.Columnas = 0
        # Agregamos columnas a nuestro list control.
        self.ListCtrl.InsertColumn(0, "N", width=100)
        self.ListCtrl.InsertColumn(1, "Desplazamientos", width=200)
        self.ListCtrl.InsertColumn(2, "Fuerza 10⁴N", width=200)

    def Agregar(self, event):
        """Metodo que agregara los datos ingresados por el usuario."""
        # Agremamos una fila al ListCtrl
        self.ListCtrl.InsertStringItem(self.Columnas, str(self.Columnas + 1))
        # Agregamos los datos a la fila agregada
        self.ListCtrl.SetStringItem(self.Columnas,
                                    1, str(self.txtDespl.GetValue()))
        self.ListCtrl.SetStringItem(self.Columnas,
                                    2, str(self.txtFuerza.GetValue()))
        self.Columnas += 1
        # Limpiamos los TextCtrl
        self.txtDespl.SetValue("")
        self.txtFuerza.SetValue("")
        self.txtDespl.SetFocus()


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
