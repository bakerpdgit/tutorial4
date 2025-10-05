def calculate_sphere_volume(radius):
    pi = 3.14159265
    return radius ** 3 * 4 * pi / 3


def calculate_vase_volume(radius, height):
    # The vase is (approximately) a cylinder on top of a sphere. The glass is 0.5cm thick which reduces the internal
    # radius; we are calculating internal volume
    internal_radius = radius - 0.5
    cylinder_height = height - radius
    sphere_volume = calculate_sphere_volume(internal_radius)
    pi = 3.14159265
    cylinder_volume = internal_radius ** 2 * pi * cylinder_height
    return sphere_volume + cylinder_volume


print(calculate_vase_volume(int(input("Enter radius: ")), int(input("Enter height: "))))
