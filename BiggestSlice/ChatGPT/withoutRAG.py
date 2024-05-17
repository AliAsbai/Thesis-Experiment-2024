import math

# Function to convert degrees, minutes, seconds to radians
def dms_to_radians(degrees, minutes, seconds):
    return math.radians(degrees + minutes / 60 + seconds / 3600)

# Function to calculate the area of the largest slice
def largest_slice_area(r, n, a_deg, a_min, a_sec):
    # Convert angle to radians
    angle = dms_to_radians(a_deg, a_min, a_sec)

    # Calculate the angle for each slice
    slice_angle = 2 * math.pi / n

    # Initialize maximum slice area
    max_slice_area = 0

    # Calculate the area of each slice
    for _ in range(n):
        slice_area = 0.5 * r ** 2 * (2 * math.sin(slice_angle / 2))
        max_slice_area = max(max_slice_area, slice_area)
        # Update angle for the next slice
        r = r * math.cos(angle / 2)

    # Return the maximum slice area
    return max_slice_area

# Main function
def main():
    # Input number of test cases
    m = int(input().strip())

    # Process each test case
    for _ in range(m):
        # Input data for each test case
        r, n, a_deg, a_min, a_sec = map(int, input().split())

        # Calculate and output the area of the largest slice
        print("{:.6f}".format(largest_slice_area(r, n, a_deg, a_min, a_sec)))

# Execute main function
if __name__ == "__main__":
    main()
