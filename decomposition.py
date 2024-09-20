def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def print_rectangle_properties(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f"Area: {area}, Perimeter: {perimeter}")
    
print_rectangle_properties(5, 3)
