area = 0 #global variable, this can be used everywhere

def calculate_square_area(side: int = 1) -> int:
    global area #try to avoid global variables in functions
    area = side * side #local variable
    print(f"The area is {area}")
    return area

calculate_square_area()
#print(f"The area of the square is {area}") you can not use the variable area outside of the function


#  extra code 

calculate_square_area(5)
print(f"The area is {area}")

""""
def build_ferrari(color = "red"):
    print(f"Built a {color} Ferrari")

build_ferrari("blue")
build_ferrari()
"""
