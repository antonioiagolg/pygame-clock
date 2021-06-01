import math

def map_range(value, left_min, left_max, right_min, right_max):
    delta_left = left_max - left_min
    delta_right = right_max - right_min

    value_scaled = (value - left_min) / delta_left

    return right_min + (value_scaled * delta_right)

def circle_point(center_point, circle_radius, radians):
    x = center_point[0] - circle_radius * math.sin(math.pi + radians)
    y = center_point[1] + circle_radius * math.cos(math.pi + radians)
    return (x, y)