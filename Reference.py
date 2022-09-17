"""Reference.py -> My reference Manim Community program
Main user functions:

CreateGlobalAxes(scale=__GlobalScale__, x_scale=__GlobalXScale__, y_scale=__GlobalYScale__, x_offset=None, y_offset=None, x_interval=1, y_interval=1, axis_color=GREEN) -> Creates standard axes
create_vector(x, y) -> Creates 2d Manim vector based off of x and y
create_arrow(end, colour, start=ORIGIN, buff=0) -> Creates Arrow starting in ORIGIN and ending in vector or mobject end
create_label(mobject, label_text, color, direction=None, buff=0, font_size=16) -> Creates Text next to mobject with specified direction and buff and colour


Main user classes:

class MainConstruct(Scene) -> Main Scene constructor with construct(self)


Main user variables:

__GlobalScale__ -> Global scalar for determining size
__GlobalXScale__ -> Global x scalar for determining x axis sizes
__GlobalYScale__ -> Global y scalar for determining y axis sizes
"""

import math
import numpy as np
from manim import *

#Create global scalar, and global x and y scalars
__GlobalScale__ = 1
__GlobalXScale__ = 1
__GlobalYScale__ = 1

def CreateGlobalAxes(scale=__GlobalScale__, x_scale=__GlobalXScale__, y_scale=__GlobalYScale__, x_offset=None, y_offset=None, x_interval=1, y_interval=1, axis_color=GREEN):
	#Temporary x scalar and y scalar
	t_x_scale = scale*x_scale
	t_y_scale = scale*y_scale
	
	#Default x_offset from -6*scale to 6*scale
	if x_offset == None:
		x_offset = [-6*t_x_scale, 6*t_x_scale]
		
	#Default y_offset from -3*scale to 3*scale
	if y_offset == None:
		y_offset = [-3*t_y_scale, 3*t_y_scale]
	
	#Calculate final x and y range
	_x_range = [x_offset[0], x_offset[1], x_interval]
	_y_range = [y_offset[0], y_offset[1], y_interval]
	
	return Axes(
					x_range=_x_range,
					y_range=_y_range,
					axis_config={"color": axis_color},
					x_axis_config={
						"numbers_to_include": np.arange(_x_range[0], _x_range[1], 2*_x_range[2]),
						"numbers_with_elongated_ticks": np.arange(_x_range[0], _x_range[1], 2*_x_range[2]),
					},
					y_axis_config={
						"numbers_to_include": np.arange(_y_range[0], _y_range[1], 2*_y_range[2]),
						"numbers_with_elongated_ticks": np.arange(_y_range[0], _y_range[1], 2*_y_range[2]),
					},
					tips=False,
				)

def create_vector(x, y):
	#Calculate vectors with respect to __GlobalScale__ and global x and y scalars (I don't know how to create np.ndarrays, so I utilize RIGHT and UP vectors)
	return RIGHT*x/(__GlobalXScale__*__GlobalScale__) + UP*y/(__GlobalYScale__*__GlobalScale__)

def create_arrow(end, colour, start=ORIGIN, buff=0):
	#Create Arrow mobject with reference to end vector or end mobject, and specified colour
	return Arrow(start=start, end=end, buff=buff, color=colour)

def create_label(mobject, label_text, colour, direction=None, buff=0, font_size=16):
	#Default direction to [1,1,0]
	if type(direction) == type(None):
		direction = create_vector(1, 1)
	#Create Text with reference to mobject and with the given text and colour
	return Text(label_text, font_size=font_size, color=colour).next_to(mobject, direction, buff)

class MainConstruct(Scene):
	def construct(self):
		
		#Create axes with label
		axes = CreateGlobalAxes()
		axes_labels = axes.get_axis_labels()
		
		#Define variables
		radiant = 1
		big_radius= 1.75
		
		coords = create_vector(1.75, 2)
		circle_offset = create_vector(1, 1)
		
		#Create circles
		circle			= Circle(radius=1, color=RED)
		big_circle		= Circle(radius=big_radius, color=BLUE)
		shifted_circle	= Circle(radius=big_radius, color=YELLOW).shift(coords)
		end_circle		= Circle(radius=big_radius, color=PINK).shift(coords)
		
		#Create circle labels
		circle_label			= create_label(circle, "c(t)=(cos(t) ; sin(t))", RED)
		big_circle_label		= create_label(big_circle, "r(t)=(r*cos(t) ; r*sin(t))", BLUE)
		shifted_circle_label	= create_label(shifted_circle, "c(t)=(a;b)+(r*cos(t) ; r*sin(t))", YELLOW)
		end_label				= create_label(shifted_circle, "c(t)=(a+r*cos(t) ; b+r*sin(t))", PINK)
		
		#Create dots
		dot			= Dot(radius=0.05, color=BLUE)
		shifted_dot	= Dot(radius=0.05, color=YELLOW)
		end_dot		= Dot(radius=0.05, color=PINK)
		
		dot.set_x(big_radius*math.cos(radiant))
		dot.set_y(big_radius*math.sin(radiant))
		
		shifted_dot.set_x(coords[0]+big_radius*math.cos(radiant))
		shifted_dot.set_y(coords[1]+big_radius*math.sin(radiant))
		
		end_dot.move_to(shifted_dot)
		
		#Create arrows
		arrow			= create_arrow(dot, BLUE)
		shifted_arrow	= create_arrow(dot, YELLOW).shift(coords)
		end_arrow		= create_arrow(dot, PINK).shift(coords)
		
		#Create VGroups
		axes_group = VGroup(axes, axes_labels)
		
		base_group	= VGroup(circle, circle_label)
		one_group	= VGroup(big_circle, big_circle_label, dot, arrow)
		two_group	= VGroup(shifted_circle, shifted_circle_label, shifted_dot, shifted_arrow)
		end_group	= VGroup(end_circle, end_label, end_dot, end_arrow)
		
		#Create/play scenes
		self.add(axes_group)
		self.add(base_group)
		
		self.wait()
		
		self.next_section()
		
		self.play(Transform(base_group, one_group))
		
		self.wait()
		
		self.next_section()
		
		self.play(Transform(base_group, two_group))
		
		self.wait()
		
		self.next_section()
		
		self.play(Transform(base_group, end_group))
		
		self.wait()
		
		self.next_section()
