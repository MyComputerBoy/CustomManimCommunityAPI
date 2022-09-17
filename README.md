# CustomManimCommunityAPI
My own custom Manim Community API

I created my own Manim Community API for creating Manim scrips easier and better to read


Reference.py -> My reference Manim Community program
Main user functions:

CreateGlobalAxes(scale=__GlobalScale__, x_scale=__GlobalXScale__, y_scale=__GlobalYScale__, x_offset=None, y_offset=None, x_interval=1, y_interval=1, axis_color=GREEN) -> Creates standard axes
create_vector(x, y) -> Creates 2d Manim vector based off of x and y
create_arrow(end, colour, start=ORIGIN, buff=0) -> Creates Arrow starting in ORIGIN and ending in vector or mobject end
create_label(mobject, label_text, color, direction=None, buff=0, font_size=16) -> Creates Text next to mobject with specified direction and buff and colour


Main user classes:

class MainConstruct(Scene) -> Main Scene constructor with construct(self)
