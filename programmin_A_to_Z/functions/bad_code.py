print("Rectangle calculator")

length = 21
width = 12

area = length * width
print(f"The area of a rectange with length {length} and width {width} is {area}")

# DRY: don't repeat yourself if you need the same piece of code multiple times, create a function
"""
def function_name(parameter1 : expression, parameter2, .... parameter_n):
    return value

if a function does not expect input, you can leave the parameters empty
"""
length = 5
width = 7

area = length * width
print(f"The area of a rectange with length {length} and width {width} is {area}")

#some other code between

length = 9
width = 11

area = length * width
print(f"The area of a rectange with length {length} and width {width} is {area}")
