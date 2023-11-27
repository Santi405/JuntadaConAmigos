from colored import fg, bg, attr, colored

# Definir códigos de colores
color_red = fg('red')
bg_grey = bg('grey_46')  # Puedes probar con 'white' o 'grey' según tu terminal
color_reset = attr('reset')

# Ejemplo de uso con el método colored() y cambio de fondo y texto
print(color_red + "Texto rojo sobre fondo gris" + color_reset)
