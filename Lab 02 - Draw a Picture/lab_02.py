

# Import the "arcade" library
import arcade

arcade.open_window(800, 600, "Drawing Example")

# color de fondo
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# inciamos la renderzacion
arcade.start_render()


# dibujo un rio
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.LIGHT_BROWN)

arcade.draw_lrtb_rectangle_filled(0, 800, 80, 0, arcade.color.BABY_BLUE)

arcade.draw_lrtb_rectangle_filled(0, 800, 20, 0, arcade.color.LIGHT_BROWN)

# dibujo un sol
arcade.draw_circle_filled(680, 540, 60, arcade.color.YELLOW)

#dibujo unas nubes
arcade.draw_circle_filled(540, 540, 40, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(510, 540, 30, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(480, 540, 40, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(450, 540, 30, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(420, 540, 40, arcade.color.PASTEL_BLUE)

arcade.draw_circle_filled(300, 540, 40, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(270, 540, 30, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(240, 540, 40, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(210, 540, 30, arcade.color.PASTEL_BLUE)
arcade.draw_circle_filled(180, 540, 40, arcade.color.PASTEL_BLUE)

# dibujo el tronco del arbol
arcade.draw_rectangle_filled(580, 175, 25, 90, arcade.color.BROWN)
# dibujo la copa del arbol
arcade.draw_circle_filled(580, 270, 80, arcade.color.MOSS_GREEN)

# dibujo el tronco del arbol
arcade.draw_rectangle_filled(340, 175, 25, 90, arcade.color.BROWN)
# dibujo la copa del arbol
arcade.draw_circle_filled(340, 270, 80, arcade.color.MOSS_GREEN)

# dibujo el tronco del arbol
arcade.draw_rectangle_filled(400, 175, 25, 90, arcade.color.BROWN)
# dibujo la copa del arbol
arcade.draw_circle_filled(400, 270, 80, arcade.color.MOSS_GREEN)

# dibujo el tronco del arbol
arcade.draw_rectangle_filled(440, 175, 25, 90, arcade.color.BROWN)
# dibujo la copa del arbol
arcade.draw_circle_filled(440, 270, 80, arcade.color.MOSS_GREEN)

# dibujo el tronco del arbol
arcade.draw_rectangle_filled(500, 175, 25, 90, arcade.color.BROWN)
# dibujo la copa del arbol
arcade.draw_circle_filled(500, 270, 80, arcade.color.MOSS_GREEN)
# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()