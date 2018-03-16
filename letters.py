import numpy

value_to_write = 1

def lettersize():
	return 5

def blank_letter():
	s=[5,5]
	L=numpy.zeros(s, dtype=(numpy.int16))
	return L

def letter_k():
	L=blank_letter()
	L[:,0] = L[2,1] = L[:,2] = L[4,2:] = L[0,2:] = L[2,4] = value_to_write
	return L

def letter_l():
	L=blank_letter()
	L[:,0] = L[4,:] = value_to_write
	return L

def letter_m():
	L=blank_letter()
	L[:,0] = L[0,:] = L[:,4] = L[:3,2] = L[4,2] = value_to_write
	return L

def letter_g():
	L=blank_letter()
	L[:,0] = L[0,:] = L[4,:] = L[2:,4] = L[2,2:] = value_to_write
	return L

def letter_r():
	L=blank_letter()
	L[:,0] = L[0,:] = L[2,:] = L[:2,4] = L[2:,2] = L[4,2:] = value_to_write
	return L

def letter_v():
	L=blank_letter()
	L[:,0] = L[0,:] = L[2,:] = L[4,:] = L[:,4] = value_to_write
	return L

def letter_t():
	L=blank_letter()
	L[0,:] = L[:,2] = value_to_write
	return L

def letter_x():
	L=blank_letter()
	L[:,2] = L[2,:] = value_to_write
	return L

def letter_e():
	L=blank_letter()
	L[:,0] = L[0,:] = L[2,:] = L[4,:] = value_to_write
	return L

def letter_o():
	L=blank_letter()
	L[:,0] = L[0,:] = L[:,4] = L[4,:] = L[2,2] = value_to_write
	return L

def letter_p():
	L=blank_letter()
	L[:,0] = L[0,:] = L[2,:] = L[:2,4] = value_to_write
	return L
