#Prompt the user for an expression
expression = input("Expression: ")

#Convert expression into variables and changing them to float
x, y, z = expression.split(" ")

#Putting x and z into floats
x = float(x)
z = float(z)

#Calculations
if y == "+":
    result = x + z

if y == "-":
    result = x - z

if y == "*":
    result = x * z

if y == "/":
    result = x / z

print(result)