# -*- coding: utf-8 -*-
"""El siguente programa."""

# Importamos las librerias necesarias para el uso de ventanas
import wx
import wx.xrc
# Importamos librerias para uso de graficos y arreglos

# Importamos el formulario
import form_ecuacion

class Ecuacion(form_ecuacion.frmEcuacion):
    """Clase principal para las ecuaciones."""

    def __init__(self, parent):
        """Constructor de la clase"""
        form_ecuacion.frmEcuacion.__init__(self, parent)
        # Agregamos columas a los ListCtrl
        self.ListCtrl_Lineal.InsertColumn(1, "Feurza(x)", width=95)
        self.ListCtrl_Lineal.InsertColumn(2, "Desplazamiento(y)", width=150)
        self.ListCtrl_Lineal.InsertColumn(3, "XiYi", width=85)
        self.ListCtrl_Lineal.InsertColumn(4, "X²", width=85)
        self.ListCtrl_Lineal.InsertColumn(5, "Y²", width=85)

        self.ListCtrl_Total_Lineal.InsertColumn(1, "Feurza(x)", width=95)
        self.ListCtrl_Total_Lineal.InsertColumn(2, "Desplazamiento(y)",
                                                width=150)
        self.ListCtrl_Total_Lineal.InsertColumn(3, "XiYi", width=85)
        self.ListCtrl_Total_Lineal.InsertColumn(4, "X²", width=85)
        self.ListCtrl_Total_Lineal.InsertColumn(5, "Y²", width=85)

        self.ListCtrl_No_Lineal.InsertColumn(1, "Feurza(x)", width=95)
        self.ListCtrl_No_Lineal.InsertColumn(2, "Desplazamiento(y)", width=130)
        self.ListCtrl_No_Lineal.InsertColumn(3, "Ln(x)", width=80)
        self.ListCtrl_No_Lineal.InsertColumn(4, "Ln(x)²", width=80)
        self.ListCtrl_No_Lineal.InsertColumn(5, "Ln(x).(y)", width=90)
        self.ListCtrl_No_Lineal.InsertColumn(6, "Y²", width=75)

        self.ListCtrl_Total_No_Lineal.InsertColumn(1, "Feurza(x)", width=95)
        self.ListCtrl_Total_No_Lineal.InsertColumn(2, "Desplazamiento(y)",
                                                   width=130)
        self.ListCtrl_Total_No_Lineal.InsertColumn(3, "Ln(x)", width=80)
        self.ListCtrl_Total_No_Lineal.InsertColumn(4, "Ln(x)²", width=80)
        self.ListCtrl_Total_No_Lineal.InsertColumn(5, "Ln(x).(y)", width=90)
        self.ListCtrl_Total_No_Lineal.InsertColumn(6, "Y²", width=75)


class MyApp(wx.App):
    """Instanciamos el formulario Principal."""

    def OnInit(self):
        """Metodo que mostrara nuestro formulario en pantalla."""
        frame1 = Ecuacion(None)
        self.SetTopWindow(frame1)
        frame1.Show()
        return 1


# end of class MyApp
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
