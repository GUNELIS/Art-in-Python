import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mplt_color
import math
from shapes import Circle, Square, Triangle

class PrimitiveArt:

    def __init__(self):
        self.shapes = []
        self.x_lim = 10
        self.y_lim = 10

    """
    The Following functions are there to add circles, sqaures and triangles related
    to the 'shape' object I've created.
    """
    def add_circle(self, x_center, y_center, radius, color='g'):
        self.shapes.append(Circle(x_center, y_center, radius, color))

    def add_square(self, x_top_left, y_top_left, side, color='r'):
        self.shapes.append(Square(x_top_left, y_top_left, side, color))

    def add_triangle(self, top_x, top_y, side_length, color='b'):
        self.shapes.append(Triangle(top_x, top_y, side_length, color))

    def visualize(self):
        """
        This function makes sure to show on the canvas all the shapes in the
        shapes list. This is done by using the matplotlib 'patches' to
        add the shapes. 
        """
        fig, ax = plt.subplots(figsize=(10, 8))
        for shape in self.shapes:
            if isinstance(shape, Circle):
                circle = patches.Circle((shape.center_x, shape.center_y), 
                                        shape.radius, 
                                        edgecolor=shape.color,
                                        facecolor='none',
                                        linewidth=2)
                ax.add_patch(circle)
            elif isinstance(shape, Square):
                # we add the same side twice to make a sqaure
                square = patches.Rectangle((shape.top_left_x, shape.top_left_y), 
                                           shape.side, 
                                           shape.side, 
                                           edgecolor=shape.color,
                                           facecolor='none',
                                           linewidth=2)
                ax.add_patch(square)
            elif isinstance(shape, Triangle):
                triangle_points = [(shape.top_x, shape.top_y), 
                                   (shape.left_x, shape.left_y), 
                                   (shape.right_x, shape.right_y)]
                triangle = patches.Polygon(triangle_points, 
                                           edgecolor = shape.color,
                                           facecolor='none',
                                           linewidth=2)
                ax.add_patch(triangle)
        
        ax.set_aspect('equal')
        ax.set_xlim([0, self.x_lim])
        ax.set_ylim([0, self.y_lim])
        plt.show()

    def get_beautiful_score(self):
        """
        This function is used to measure the beauty of each art work.
        To do so, the overall area of all the shapes in the canvas is measured
        as well as the total area for each shape. 
        If the volume ratio for all three shapes is the same then the piece is considered
        100 % beautiful. 
        If there is only one of the shapes, the value will automatically be 33.33%.

        """

        if not self.shapes:  # If the list of shapes is empty
            return 0
        
        total_area = 0
        circle_area = 0
        square_area = 0
        triangle_area = 0
        
        for shape in self.shapes:
            # adding the circle area
            if isinstance(shape, Circle):
                circle_area += math.pi * shape.radius ** 2
            # adding the sqaure area
            elif isinstance(shape, Square):
                square_area += shape.side ** 2
            # adding the triangle area
            elif isinstance(shape, Triangle):
                triangle_area += (math.sqrt(3)/4) * shape.side_length ** 2

        # calculate the proportion of each shape's area to the total area
        total_area = circle_area + square_area + triangle_area
        circle_ratio = circle_area / total_area
        square_ratio = square_area / total_area
        triangle_ratio = triangle_area / total_area
        
        # here we check if there is only one shapes present which should yield a 33.33 beauty score
        shape_counts = 0
        for area in (circle_area,square_area,triangle_area):
            if area > 0: # if this shape contains more than one object
                shape_counts+=1

        if shape_counts == 1:        
            return 33.33
        
        
        # each ratio is subtracted by 1/3 and then the sum is turned into a % in the next line
        average_diff = (abs(1/3 - circle_ratio) + abs(1/3 - square_ratio) + abs(1/3 - triangle_ratio)) / 3

        score = (1 - average_diff) * 100

        # ensures score is between 0 and 100
        return max(0, min(score,100))  
         
    
    def convert_to_circle(self, shape):
        """
        This function simply turns squares and triangles into circles.
        The function takes in a shape as an argument and extracts its
        area and centriod. Then the radius of the circle can be calculates
        by the area and the centroid gives the center of the circle. 
        """ 
        # if its already a circle we quickly return as is
        if isinstance(shape, Circle):
            return shape 
         
        # if its a sqaure, we extract the area by multiplying the sides
        # and the centroid by dividing the side by 2 added to the x
        if isinstance(shape, Square):
            area = shape.side ** 2
            center_x = shape.top_left_x + shape.side / 2
            center_y = shape.top_left_y + shape.side / 2

        # if its a triangle, we use the appropiate formulas
        # similiar to the previuos step just with triangles
        elif isinstance(shape, Triangle):
            area = (math.sqrt(3)/4) * shape.side_length ** 2
            center_x = (shape.top_x + shape.left_x + shape.right_x) / 3
            center_y = (shape.top_y + shape.left_y + shape.right_y) / 3

        # use the calculated area to determine the radius 
        radius = math.sqrt(area / math.pi)
            
        return Circle(center_x, center_y, radius, shape.color)

    def circulate(self):
        for index, shape in enumerate(self.shapes):
            self.shapes[index] = self.convert_to_circle(shape)


    def rnd_draw(self, min_per_shape =6):
        """
        This function creates a drawing by randomizing its components.
        It takes in as an argument the exact number of 
        objects to randomize for each of the three shapes. So in total,
        there would be input_number*3 shapes on the canvas. 
        """
        self.shapes = []

        # for the circle we get the center(x,y), radius and color
        for i in range(min_per_shape):
            rnd_radius = random.choice(range(0, self.x_lim-3))
            rnd_x = random.choice(range(0, self.x_lim))
            rnd_y = random.choice(range(0, self.y_lim))
            rnd_color = random.choice(list(mplt_color.cnames))
            self.add_circle(rnd_x,rnd_y,rnd_radius,rnd_color)
        
        # for the sqaure we get the NortWest(x,y), side length and color
        for i in range(min_per_shape):
            rnd_x = random.choice(range(0, self.x_lim))
            rnd_y = random.choice(range(0, self.y_lim))
            rnd_side = random.choice(range(0, self.x_lim-3))
            rnd_color = random.choice(list(mplt_color.cnames))
            self.add_square(rnd_x,rnd_y,rnd_side,rnd_color)

        # for the triangle we get the top(x,y), side length and color
        for i in range(min_per_shape):
            rnd_x = random.choice(range(0, self.x_lim))
            rnd_y = random.choice(range(0+3, self.y_lim))
            rnd_side = random.choice(range(0, self.x_lim-3))
            rnd_color = random.choice(list(mplt_color.cnames))
            self.add_triangle(rnd_x,rnd_y,rnd_side,rnd_color)

