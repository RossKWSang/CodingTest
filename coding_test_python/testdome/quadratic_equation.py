from math import sqrt


def quadratic_equation(a, b, c):
    return int((-b + sqrt(b**2 - 4*a*c))/(2*a)), int((-b - sqrt(b**2 - 4*a*c))/(2*a))

print(quadratic_equation(2, 10, 8))
