class Shape:
    """
    This is the basic object that will be created, customized and finally visualized.
    The different indivdal shape classes inherit this class and have their own individual
    qualities. 
    """
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, x, y, radius, color='r'):
        super().__init__(color)
        self.center_x = x
        self.center_y = y
        self.radius = radius

class Square(Shape):
    def __init__(self, x, y, side, color='b'):
        super().__init__(color)
        self.top_left_x = x
        self.top_left_y = y
        self.side = side

class Triangle(Shape):
    # Here, we can use the top vertex and side length to determine the other two vertices
    # for an equilateral triangle.
    def __init__(self, top_x, top_y, side_length, color='g'):
        super().__init__(color)
        self.top_x = top_x
        self.top_y = top_y
        self.side_length = side_length
        self.left_x = top_x - (side_length / 2)
        self.left_y = top_y - (side_length * (3**0.5 / 2))
        self.right_x = top_x + (side_length / 2)
        self.right_y = self.left_y
