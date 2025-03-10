from myapp.mymodule.funcs import multiply, divide


def multiply_by_two(x):
    return multiply(x, 2)


def divide_by_two(x):
    return divide(x, 2)

# New function to calculate the area of a square
def area_of_square(side):
    return multiply(side, side)  # side * side