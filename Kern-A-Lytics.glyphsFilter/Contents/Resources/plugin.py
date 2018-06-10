# encoding: utf-8

###########################################################################################################
#
#
#	Filter with dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20with%20Dialog
#
#	For help on the use of Interface Builder:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import traceback
from robofab.world import RFont

from kernGraph import FlexibleWindow

class KernGraph(FilterWithDialog):
		
	def settings(self):
		self.menuName = "Kern-A-Lytics"
	
	# On dialog show
	def start(self):
		pass
	
	# Actual filter
	def runFilterWithLayer_error_(self, layer, error):
		font = layer.font()
		return self.showWindow(font)
	
	def runFilterWithLayers_error_(self, layers, error):
		font = layers[0].font()
		return self.showWindow(font)
	
	def showWindow(self, font):
		try:
			a = []
			for idx in range(len(font.masters)):
				a.append(RFont(font, idx))
			FlexibleWindow(a)
		except:
			import traceback
			print traceback.format_exc()
		return (True, None)
	
	def process_(self, sender):
		pass
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
