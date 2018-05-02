# Physics 91SI
# Spring 2018
# Lab9

import numpy as numpy
import particle

class Molecule:
	'''Stores information about a diatomic molecule'''

	def __init__(self, p1_pos, p1_mass, p2_pos, p2_mass, k, L0):
		'''Create diatomic molecule'''
		self.p1 = particle.Particle(p1_pos, p1_mass)
		self.p2 = particle.Particle(p2_pos, p2_mass)
		self.k = k
		self.L0 = L0

	def get_displ(self):
		'''Returns vector points from p1 to p2'''
		return self.p2.pos - self.p1.pos

	def get_force(self):
		'''Returns the force (vector) due to the spring on p1'''
		return self.k * self.get_displ()



