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
## Class frmEcuacion
###########################################################################

class frmEcuacion ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 691,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		gridPrincipal = wx.FlexGridSizer( 5, 1, 0, 0 )
		gridPrincipal.SetFlexibleDirection( wx.BOTH )
		gridPrincipal.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gridLineal = wx.FlexGridSizer( 5, 4, 0, 0 )
		gridLineal.SetFlexibleDirection( wx.BOTH )
		gridLineal.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		gridLineal.AddSpacer( ( 60, 0), 1, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Regresion Lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gridLineal.Add( self.m_staticText6, 0, wx.ALL, 5 )


		gridLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridLineal.AddSpacer( ( 60, 0), 1, wx.EXPAND, 5 )


		gridLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ListCtrl_Lineal = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,150 ), wx.LC_REPORT )
		gridLineal.Add( self.ListCtrl_Lineal, 0, wx.ALL, 5 )


		gridLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gridLineal.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.ListCtrl_Total_Lineal = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,55 ), wx.LC_REPORT )
		gridLineal.Add( self.ListCtrl_Total_Lineal, 0, wx.ALL, 5 )


		gridLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridPrincipal.Add( gridLineal, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Ecuacion lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer3.Add( self.m_staticText14, 0, wx.ALL, 10 )

		self.txtEcuacionLineal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer3.Add( self.txtEcuacionLineal, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Evaluar Punto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer3.Add( self.m_staticText15, 0, wx.ALL, 10 )

		self.txtEvaluarPunto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.txtEvaluarPunto, 0, wx.ALL, 5 )

		self.btnEvaluarPunto = wx.Button( self, wx.ID_ANY, u"Evaluar punto", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnEvaluarPunto, 0, wx.ALL, 5 )


		gridPrincipal.Add( bSizer3, 1, wx.EXPAND, 5 )

		gridNoLineal = wx.FlexGridSizer( 5, 4, 0, 0 )
		gridNoLineal.SetFlexibleDirection( wx.BOTH )
		gridNoLineal.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		gridNoLineal.AddSpacer( ( 60, 0), 1, wx.EXPAND, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Regresion no lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		gridNoLineal.Add( self.m_staticText61, 0, wx.ALL, 5 )


		gridNoLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridNoLineal.AddSpacer( ( 60, 0), 1, wx.EXPAND, 5 )


		gridNoLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ListCtrl_No_Lineal = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,150 ), wx.LC_REPORT )
		gridNoLineal.Add( self.ListCtrl_No_Lineal, 0, wx.ALL, 5 )


		gridNoLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridNoLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		gridNoLineal.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.ListCtrl_Total_No_Lineal = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,55 ), wx.LC_REPORT )
		gridNoLineal.Add( self.ListCtrl_Total_No_Lineal, 0, wx.ALL, 5 )


		gridNoLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridNoLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridNoLineal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gridPrincipal.Add( gridNoLineal, 1, wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"Ecuacion no lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		bSizer31.Add( self.m_staticText141, 0, wx.ALL, 10 )

		self.txtEcuacionNoLineal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer31.Add( self.txtEcuacionNoLineal, 0, wx.ALL, 5 )

		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"Evaluar Punto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		bSizer31.Add( self.m_staticText151, 0, wx.ALL, 10 )

		self.txtEvaluarPuntoNoLineal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.txtEvaluarPuntoNoLineal, 0, wx.ALL, 5 )

		self.btnEvaluarPuntoNoLineal = wx.Button( self, wx.ID_ANY, u"Evaluar punto", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.btnEvaluarPuntoNoLineal, 0, wx.ALL, 5 )


		gridPrincipal.Add( bSizer31, 1, wx.EXPAND, 5 )


		self.SetSizer( gridPrincipal )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnEvaluarPunto.Bind( wx.EVT_BUTTON, self.Evaluar_punto )
		self.btnEvaluarPuntoNoLineal.Bind( wx.EVT_BUTTON, self.Evaluar_punto_No_Lineal )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Evaluar_punto( self, event ):
		event.Skip()

	def Evaluar_punto_No_Lineal( self, event ):
		event.Skip()
