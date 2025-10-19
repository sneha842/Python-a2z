#Topic : Operator and Operand
# Goal: Start Python-A2Z daily practice

print("Arithmetic Operators: ")
a = int(input("Enter first number: ")) #user input
b = int(input("Enter second number: "))
print("a+b: ",a+b)
print("a-b: ",a-b)
print("a*b: ",a*b)
print("a/b: ",a/b)
print("a//b: ",a//b)
print("a**b: ",a**b)
print("a%b: ",a%b)

print("Comparision Operators: ")
print("a==b: ",a==b)
print("a!=b: ",a!=b)
print("a>b: ",a>b)
print("a<b: ",a<b)
print("a>=b: ",a>=b)
print("a<=b: ",a<=b)

print("Bitwise Operators: ")
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 1 =", a << 1) # Left Shift
print("a >> 1 =", a >> 1) # Right Shift

print(" Logical Operators: ")
x = bool(int(input("Enter 1 for True, 0 for False (x): ")))
y = bool(int(input("Enter 1 for True, 0 for False (y): ")))

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)