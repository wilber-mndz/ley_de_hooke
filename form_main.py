# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 15 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class form1
###########################################################################

class form1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 680,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		fgSizer6 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer1 = wx.FlexGridSizer( 2, 7, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer1.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Ley de Hooke", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Desplazamientos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtDespl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtDespl, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Fuerza 10⁴N", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtFuerza = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtFuerza, 0, wx.ALL, 5 )

		self.btnAgregar = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnAgregar, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )


		fgSizer6.Add( fgSizer1, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer8.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.ListCtrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), wx.LC_EDIT_LABELS|wx.LC_REPORT )
		fgSizer8.Add( self.ListCtrl, 0, wx.ALL, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.btnEliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnEliminar, 0, wx.ALL, 5 )

		self.btnNuevo = wx.Button( self, wx.ID_ANY, u"Nuevo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnNuevo.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )

		bSizer1.Add( self.btnNuevo, 0, wx.ALL, 5 )


		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnCalcular = wx.Button( self, wx.ID_ANY, u"Calcular", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnCalcular, 0, wx.ALL, 5 )


		fgSizer8.Add( bSizer1, 1, wx.EXPAND, 5 )


		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer6.Add( fgSizer8, 1, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 2, 6, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer4.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.label1 = wx.StaticText( self, wx.ID_ANY, u"Ecuacion lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )
		fgSizer4.Add( self.label1, 0, wx.ALL, 15 )

		self.txtEcuLineal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer4.Add( self.txtEcuLineal, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Ecuacion no lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer4.Add( self.m_staticText5, 0, wx.ALL, 15 )

		self.txtEcuNoLin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer4.Add( self.txtEcuNoLin, 0, wx.ALL, 5 )


		fgSizer4.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )


		fgSizer4.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.btnMostrar = wx.Button( self, wx.ID_ANY, u"Mostrar gráfica", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnMostrar, 0, wx.ALL, 5 )


		fgSizer6.Add( fgSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.txtDespl.Bind( wx.EVT_TEXT, self.Validar_Despl )
		self.txtFuerza.Bind( wx.EVT_TEXT, self.Validar_Fuerza )
		self.btnAgregar.Bind( wx.EVT_BUTTON, self.Agregar )
		self.ListCtrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.Seleccionar )
		self.btnEliminar.Bind( wx.EVT_BUTTON, self.Eliminar )
		self.btnNuevo.Bind( wx.EVT_BUTTON, self.Nuevo )
		self.btnCalcular.Bind( wx.EVT_BUTTON, self.Calcular )
		self.btnMostrar.Bind( wx.EVT_BUTTON, self.Mostrar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Validar_Despl( self, event ):
		event.Skip()

	def Validar_Fuerza( self, event ):
		event.Skip()

	def Agregar( self, event ):
		event.Skip()

	def Seleccionar( self, event ):
		event.Skip()

	def Eliminar( self, event ):
		event.Skip()

	def Nuevo( self, event ):
		event.Skip()

	def Calcular( self, event ):
		event.Skip()

	def Mostrar( self, event ):
		event.Skip()
