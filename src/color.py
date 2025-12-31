from vec3 import *

color = vec3()

def write_color(pixel_color:vec3)->str:
    red = pixel_color.x()
    green = pixel_color.y()
    blue = pixel_color.z()

    pr = int(red * 255.99)
    pg = int(green * 255.99)
    pb = int(blue * 255.99)

    return str(pr) + " " + str(pg) + " " + str(pb) + "    "