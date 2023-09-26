from logic_module import PrimitiveArt 

"""
    Use this script to create your very own custome PrimitiveArt.
    
    Commands:

        -- Adding Objects to the Canvas Manually --
            * add_circle(center_X, center_Y, radius, color)
            * add_sqaure(topLeft_X, topLeft_Y, side_length, color)
            * add_triangle(top_X, top_Y, side_length, color)
            (by default the canvas is a 10 by 10 grid , so try to input values in that range).

        -- Getting the Beauty Score --
            * get_beautiful_score() 

        -- Create Art Randomly --
            * rnd_draw(number_of_objects_per_shape)
        
        -- Visualizing --
            * visualize()
"""

# Here is an example Script you can use. 
# Enjoy!
art = PrimitiveArt()
art.rnd_draw(13) 
art.add_circle(1, 1, 0.5)
art.add_square(2, 2, 1)
art.add_triangle(4, 4, 1.461)
print("you got a beauty score of : ",art.get_beautiful_score())
art.visualize()