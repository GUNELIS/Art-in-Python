import math
import tkinter as tk
from tkinter import simpledialog, colorchooser, messagebox
from matplotlib import patches
from logic_module import PrimitiveArt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from shapes import *

"""
    This Class deals with the visual side - the GUI. As this use case does not require a great deal of 
    graphical design, I will use matplotlib for the representation and tkinter.
"""
class PrimitiveArtApp(tk.Tk):
    
    def __init__(self, art):

        super().__init__()
        # Here I am using the components of the tkinter class which it inherits.    
        self.title("Primitive Art App")
        self.geometry("1700x1700")
        self.art = art # accepting the PrimitiveArt object
        self.shape_to_draw = None  # to store which shape we're currently drawing
        self.initial_coords = None  # to store the start coordinates when drawing

        # creating the matplotlib elements and combining it with tkinter
        self.fig, self.ax = plt.subplots(figsize=(20, 10))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self) # here is the bridge between tinker and matplotlib

        # Here the buttons are needed for the users functionality, 
        # a frame is made  to hold all the buttons
        button_frame = tk.Frame(self,background='light blue')
        button_frame.grid(row=0, column=1, sticky=tk.NW)

        # Add Circle Button
        self.add_circle_btn = tk.Button(button_frame, text="Add Circle", command=self.set_draw_circle)
        self.add_circle_btn.grid(row=0, column=1, pady=10, sticky=tk.W)
        # Add Square Button
        self.add_square_btn = tk.Button(button_frame, text="Add Square", command=self.set_draw_square)
        self.add_square_btn.grid(row=1, column=1, pady=10, sticky=tk.W)
        # Add Triangle Button
        self.add_triangle_btn = tk.Button(button_frame, text="Add Triangle", command=self.set_draw_triangle)
        self.add_triangle_btn.grid(row=2, column=1, pady=10, sticky=tk.W)
        # Set Background Button
        self.set_backgrund_btn = tk.Button(button_frame, text="Change Background", command=self.change_background)
        self.set_backgrund_btn.grid(row=3, column=1, pady=10, sticky=tk.W)
        # Beauty Score Button
        self.get_score_btn = tk.Button(button_frame, text="Beauty Score", command=self.get_beautiful_score)
        self.get_score_btn.grid(row=4, column=1, pady=10, sticky=tk.W)
        # Circulate Button
        self.circulate_btn = tk.Button(button_frame, text="Circulate", command=self.circulate)
        self.circulate_btn.grid(row=5, column=1, pady=10, sticky=tk.W)
        # Randomize Button
        self.randomize_btn = tk.Button(button_frame, text="Randomize", command=self.randomize_art)
        self.randomize_btn.grid(row=6, column=1, pady=10, sticky=tk.W)
        # Clear All Button
        self.clear_all_btn = tk.Button(button_frame, text="Clear All", command=self.clear_all)
        self.clear_all_btn.grid(row=7, column=1, pady=50, sticky=tk.W)
        
        # put the canvas to the right of the button frame
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky=tk.NW) # getting original tk widget object
        # self.canvas.draw()
        self.update_plot()

        # relate the mouse events with drawing shapes for the shape creation by dragging the mouse
        self.canvas.mpl_connect('button_press_event', self.on_press)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        
        # make sure that the window closes when the exit button is pressed, quits the loop
        self.protocol("WM_DELETE_WINDOW", self.collapse_all)


    def collapse_all(self):
        self.destroy()
        self.quit()

    def clear_all(self):
        self.ax.clear()
        self.art.shapes = []  # Clear the shapes list
        self.ax.set_facecolor(color='white') # reset the background white
        self.canvas.draw()

    def change_background(self):
        chosen_color = colorchooser.askcolor()[1]  # Ask the user to pick a color
        self.ax.set_facecolor(chosen_color)
        self.canvas.draw()

    def set_draw_circle(self):
        self.shape_to_draw = "circle"
        self.chosen_color = colorchooser.askcolor()[1]  # Ask the user to pick a circle color

    def set_draw_square(self):
        self.shape_to_draw = "square"
        self.chosen_color = colorchooser.askcolor()[1]  # Ask the user to pick a square color

    def set_draw_triangle(self):
        self.shape_to_draw = "triangle"
        self.chosen_color = colorchooser.askcolor()[1]  # Ask the user to pick a triangle color

    def update_plot(self):
        """
        This functions updates the canvas whenever it is called.
        If anything is added, removed or changed this function is called in order
        to update it visualy. 
        Checks all the shapes in the shape list and then redraws them. 
        """
        self.ax.clear() # clear the canvas from any existing shapes
        self.ax.set_aspect('equal') # make sure we enforce that aspect ratio is equal (sqaures and not rectangles)

        for shape in self.art.shapes:
            if isinstance(shape, Circle):
                circle = patches.Circle((shape.center_x, shape.center_y), 
                                        shape.radius, 
                                        edgecolor=shape.color,
                                        facecolor='none',
                                        linewidth=2)
                self.ax.add_patch(circle)
            elif isinstance(shape, Square):
                square = patches.Rectangle((shape.top_left_x, shape.top_left_y), 
                                           shape.side, 
                                           shape.side, 
                                           edgecolor=shape.color,
                                           facecolor='none',
                                           linewidth=2)
                self.ax.add_patch(square)
            elif isinstance(shape, Triangle):
                triangle_points = [(shape.top_x, shape.top_y), 
                                   (shape.left_x, shape.left_y), 
                                   (shape.right_x, shape.right_y)]
                triangle = patches.Polygon(triangle_points, 
                                           edgecolor = shape.color,
                                           facecolor='none',
                                           linewidth=2)
                self.ax.add_patch(triangle)

        self.ax.set_xlim([0, 10])
        self.ax.set_ylim([0, 10])
        self.canvas.draw()

    """
    The following functions use the mouse listeners to capture the start and end locations 
    of the mouse when the user is creating a shape. These coordinates are used
    to compute the details and create the shapes.
    """
    def on_press(self, event):
        self.initial_coords = (event.xdata, event.ydata)

    def on_release(self, event):
        final_coords = (event.xdata, event.ydata)
        self.draw_new_shape(final_coords)

    
    def draw_new_shape(self, final_coords):
        """
        This function draws the shapes that the user requested by dragging the mouse
        along the grid, using the mouse listerner which documented the locations.
        Here the shapes are created , added to the list of shapes and drawmn. 
        """
        if self.shape_to_draw == "circle":
            center_x, center_y = self.initial_coords
            radius = ((center_x - final_coords[0]) ** 2 + (center_y - final_coords[1]) ** 2) ** 0.5
            self.art.add_circle(center_x, center_y, radius, self.chosen_color)

        elif self.shape_to_draw == "square":
            side = max(abs(final_coords[0] - self.initial_coords[0]), abs(final_coords[1] - self.initial_coords[1]))
            self.art.add_square(self.initial_coords[0], self.initial_coords[1], side, self.chosen_color)

        elif self.shape_to_draw == "triangle":
            top_x, top_y = self.initial_coords
            side_length = ((top_x - final_coords[0]) ** 2 + (top_y - final_coords[1]) ** 2) ** 0.5
            self.art.add_triangle(top_x, top_y, side_length, self.chosen_color)

        self.update_plot()

        # reset the chosen color and shape
        self.chosen_color = None
        self.shape_to_draw = None

    def get_beautiful_score(self):
        """
        This function retrieves the beauty score from the logic module.
        """
        score = self.art.get_beautiful_score()
        messagebox.showinfo("Beautiful Score", f"Your art's beautiful score is: {score:.2f}%")

        
    def circulate(self):
        """
        This function circulates all shapes.
        """
        self.art.circulate()
        self.update_plot()

    def randomize_art(self):
        """
        This function relates to the logic module for the randomize shape. It asks 
        the user for a value which is the number of shapes per type.
        """
        # Ask the user for the number of shapes per type
        num_shapes = simpledialog.askinteger("Input", "How many triangles, squares and circles do you want the Random Artist draw?", parent=self)
        
        if num_shapes is None:  # If the user closes the dialog or clicks cancel
            return 
        self.art.rnd_draw(num_shapes)
        self.update_plot()


if __name__ == "__main__":
    art = PrimitiveArt()
    app = PrimitiveArtApp(art)
    app.mainloop()
