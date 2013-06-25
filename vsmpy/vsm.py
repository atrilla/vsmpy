# 
# File 	  : vsm.py
# Created : 4-May-2011
# By	  : atrilla
# 
# Vector Space Model implementation
# 
# Copyright (c) 2011 Alexandre Trilla
# 
# This file is part of VSMpy.
# 
# You should have received a copy of the rights granted with this
# distribution of VSMpy. See LICENCE.
# 

from math import sqrt

"""The <i>VSM</i> is an implementation of a Vector Space Model.
   <p>
   Classical implementation (Salton et. al.).
   </p>
   @author Alexandre Trilla
"""

__docformat__ = "javadoc"

class VectorSpaceModel:

	def __init__(self):
		self.__cat = dict()
		self.__vcat = dict()
		self.__dim = []

	def input(self, text, c):
		"""Inputs a parsed training instance.
		   @param text The parsed training instance.
		   @param c The corresponding category.
		"""
		for term in text:
			# Category-wise issues
			if (self.__cat.has_key(c)):
				if (self.__cat[c].has_key(term)):
					self.__cat[c][term] += 1
				else:
					self.__cat[c][term] = 1
			else:
				self.__cat[c] = {term : 1}
			if (self.__dim.count(term) == 0):
				self.__dim.append(term)
	
	def cosine(self, text, c):
		"""Cosine similarity."""
		vtext = self.sparseVector(text)
		return self.__dot(vtext, self.__vcat[c]) / (sqrt(self.__dot(vtext, vtext) * self.__dot(self.__vcat[c], self.__vcat[c])))

	def __dot(self, v1, v2):
		"""Dot product."""
		dotp = 0
		i = 0
		while (i < len(v1)):
			dotp += v1[i] * v2[i]
			i += 1
		return dotp

	def train(self):
		"""Pre-computes things."""
		for c in self.__cat.keys():
			v = []
			for d in self.__dim:
				v.append(self.__cat[c].get(d, 0))
			self.__vcat[c] = v
	
	def sparseVector(self, text):
		"""Builds a sparse vector representation of the input
			parsed text."""
		v = []
		for d in self.__dim:
			cc = text.count(d)
			if (cc > 0):
				cc = 1
			v.append(cc)
		return v

	def parse(self, text):
		"""Parser.
		   <p>Splits the plain input text by spaces and constructs
		   a vector representation.</p>
		   @param text The plain input text.
		   @return A vector representation of the input text.
		"""
		return text.split()

