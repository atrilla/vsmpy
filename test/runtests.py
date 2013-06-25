#!/usr/bin/python
# 
# File	  : runtests.py
# Created : 14-Jul-2011
# By	  : atrilla
# 
# Testing script
# 
# Copyright (c) 2011 Alexandre Trilla
# 
# This file is part of VSMpy.
# 
# You should have received a copy of the rights granted with this
# distribution of VSMpy. See LICENCE.
# 

import vsmpy.vsm

class Test():
	def testVSM(self):
		theVSM = vsmpy.vsm.VectorSpaceModel()
		theVSM.input(theVSM.parse("I love playing football ."), "C1")
		theVSM.input(theVSM.parse("I like playing tennis ."), "C2")
		theVSM.train()
		#
		if ((theVSM.cosine(theVSM.parse("Do you enjoy playing football ?"), "C1") > theVSM.cosine(theVSM.parse("Do you enjoy playing football"), "C2")) == True):
			print "VSM ...\t OK"
		else:
			print "VSM ...\t FAILED!!!"

# conditional runs tests if this file called as script 
# (allows import w/o run)
if __name__ == '__main__':
	test = Test()
	test.testVSM()

