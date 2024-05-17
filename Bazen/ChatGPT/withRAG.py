import sys
import math

def calculate_other_endpoint(x, y):
    if x == 0 and y == 0:
        return 125.00, 125.00
    
    # Calculate the length of the hypotenuse (pool edge)
    hypotenuse_length = math.sqrt(2 * (250 ** 2))
    
    # Calculate the slope of the hypotenuse
    slope = -1  # Perpendicular slope
    
    # Calculate the midpoint of the hypotenuse
    midpoint_x = hypotenuse_length / 2
    midpoint_y = midpoint_x
    
    # Calculate the equation of the line perpendicular to the hypotenuse passing through the given point
    # Using point-slope form: y - y1 = m(x - x1)
    x1 = x
    y1 = y
    b = y1 - (-1/slope) * x1
    
    # Find the intersection point of the two lines
    # y = mx + b1 and y = -1/m * x + b2
    intersection_x = (midpoint_y - b) / (slope + 1/slope)
    intersection_y = slope * intersection_x + b
    
    return intersection_x, intersection_y

# Read input from STDIN
for line in sys.stdin:
    x, y = map(int, line.split())
    result_x, result_y = calculate_other_endpoint(x, y)
    print("{:.2f} {:.2f}".format(result_x, result_y))
