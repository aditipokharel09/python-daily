import random

# Dependency from Level 1
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# 1. List of Hex colors
def list_of_hexa_colors(count):
    hex_chars = "0123456789abcdef"
    colors = []
    for _ in range(count):
        # Pick 6 random characters from hex_chars and join them
        color = "#" + "".join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)
    return colors

# 2. List of RGB colors
def list_of_rgb_colors(count):
    # Using a list comprehension to call the Level 1 function
    return [rgb_color_gen() for _ in range(count)]

# 3. Universal generate_colors function
def generate_colors(color_type, count):
    if color_type == 'hexa':
        return list_of_hexa_colors(count)
    elif color_type == 'rgb':
        return list_of_rgb_colors(count)
    return [] # Return empty list if type is unknown