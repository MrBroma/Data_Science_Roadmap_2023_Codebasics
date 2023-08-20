import math

def find_cylinder_volume(radius, height=7):
    print("radius:", radius)
    print("height:", height)
    volume = math.pi * (radius ** 2) * height
    return round(volume)


r = 5
h = 10

print(find_cylinder_volume(r, h))