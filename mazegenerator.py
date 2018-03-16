#!/bin/python

import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import matplotlib.image as image
from letters import *

def merge(maze_matrix=0, actual_letter=0, x=0, y=0):
	sx = lettersize()
	sy = lettersize()
	for ix in range(0,sx):
		for iy in range(0,sy):
			maze_matrix[ix+x,iy+y] = actual_letter[ix,iy]
	return maze_matrix


def maze(width=200, height=200, complexity=2, density=2):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    print("density: ", density)
    print("complexity: ", complexity)
    # Build actual maze
    Z = numpy.zeros(shape, dtype=(numpy.int16))
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
#    Z[:,6] = 1
    #Z=write_kolmogorov(Z)
    Z=write_error(Z)
#    Z=numpy.logical_or(Z, L))
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    Z=write_error(Z)
    return Z

def write_kolmogorov(maze_matrix):
	lx = 2
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_k(),x=lx,y=2)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_l(),x=lx,y=8)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_m(),x=lx,y=14)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_g(),x=lx,y=20)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_r(),x=lx,y=26)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_v(),x=lx,y=32)
	lx2 = 8
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_t(),x=lx2,y=2)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_v(),x=lx2,y=8)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_x(),x=lx2,y=14)
	return maze_matrix

def write_error(maze_matrix):
	lx = 12
	ly = 12
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_e(),x=lx,y=ly)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_r(),x=lx,y=ly+6)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_r(),x=lx,y=ly+12)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_o(),x=lx,y=ly+18)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_r(),x=lx,y=ly+24)
	lx2 = 18
	ly2 = 12
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_p(),x=lx2,y=ly2)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_o(),x=lx2,y=ly2+6)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_r(),x=lx2,y=ly2+12)
	maze_matrix=merge(maze_matrix=maze_matrix,actual_letter=letter_t(),x=lx2,y=ly2+18)
	return maze_matrix

def draw_logo(i):
	print("Generating: "+str(i)+"th logo image...")
	#pyplot.figure(figsize=(10, 10))
	#pyplot.tight_layout()
	#pyplot.imshow(maze(60, 60, 1, 2), cmap=pyplot.cm.binary, interpolation='nearest')
	#pyplot.xticks([]), pyplot.yticks([])
	#pyplot.savefig(filename, frameon=True, transparent=True, bbox_inches='tight', pad_inches=0)
	Z = maze(60, 60, 1, 2)
	scaling = 8
	Z = numpy.kron(Z, numpy.ones((scaling,scaling)))
	filename="img/errorPort_logo_"+str(i)+".png"
	image.imsave(filename, Z, dpi=100, cmap=pyplot.cm.binary)
	print("Done.")
	#pyplot.show()

def draw_cover(i):
	print("Generating: "+str(i)+"th logo image...")
	Z = maze(312, 820, 1, 2)
	scaling = 1
	Z = numpy.kron(Z, numpy.ones((scaling,scaling)))
	filename="img/errorPort_cover_"+str(i)+".png"
	image.imsave(filename, Z, dpi=100, cmap=pyplot.cm.binary)
	print("Done.")

for index in range(0, 0):
	draw_logo(index)

for index in range(0,1):
	draw_cover(index)



#pyplot.figure(figsize=(10, 5))
#pyplot.imshow(maze(20, 44), cmap=pyplot.cm.binary, interpolation='nearest')
#pyplot.xticks([]), pyplot.yticks([])
#pyplot.show()
