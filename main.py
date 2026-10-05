def calculate_area(length, width):
    return length * width 

def calculate_perimeter(length, width):
    return 2 * (length + width)

def describe_rectangle(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    return f"Area: {area}, Perimeter: {perimeter}"

print(calculate_area(5, 10))
print(calculate_perimeter(5, 10))
print(describe_rectangle(5, 10))
