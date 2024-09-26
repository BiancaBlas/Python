def solve_equation(a: float, b: float, c: float) -> float:
    try:
        return (float(c) - float(b)) / float(a)
    except ZeroDivisionError:
        print("Error! 'a' can't be zero. Enter a valid value")
    except ValueError:
        print("Error! Make sure you enter numeric issue's")
    finally:
        print("Leaving solve_equation")

print("ax + b = c linear equation solver")
a = input("Enter a: ")
#if float(a) == 0:
#    raise ValueError("'a' can't be zero.")
b = input("Enter b: ")
c = input("Enter c: ")

try:
    x = solve_equation(a, b, c)
except Exception: #don't use empty except statements. Exeption makes sure we only catch mistakes by the user
    print("Something bad happend.")
else:
    print(f"x is {x}")