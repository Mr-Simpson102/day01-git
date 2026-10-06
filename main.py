def calculate_area(length, width):
    return length * width 

def calculate_perimeter(length, width):
    return 2 * (length + width)

def describe_rectangle(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    return f"Area: {area}, Perimeter: {perimeter}"

def calculate_square_area(side_length):
    return side_length ** 2

def calculate_average(numbers):
    if not numbers:
        raise ValueError("Numbers cannot be empty.")
    return sum(numbers) / len(numbers)

def triangle_area(base, height):
    return 0.5 * base * height

print(calculate_area(5, 10))
print(calculate_perimeter(5, 10))
print(describe_rectangle(5, 10))
print(calculate_square_area(5))
print(f"Triangle Area: {triangle_area(5, 10)}")
print(f"Average: {calculate_average([1, 2, 3, 4, 5])}")