from sympy import symbols, diff


x = symbols('x')


f = x**2


derivative = diff(f, x)


print("Function f(x) =", f)
print("Derivative f'(x) =", derivative)