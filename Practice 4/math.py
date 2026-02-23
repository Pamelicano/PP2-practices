from math import *

# TASK 1: Write a Python program to convert degree to radian.
degree = float(input("Input degree: "))
radians = radians(degree)
print(f"Output radian: {radians:.6f}")

#TASK 2: Write a Python program to calculate the area of a trapezoid.
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
area = (a + b) * h / 2
print(f"Output: {area}")

#TASK 4: Write a Python program to calculate the area of regular polygon.
n = int(input("Number of sides: "))
l = float(input("Length of a side: "))
area = (n * l ** 2) / (4 * tan(pi / n))
print(f"Output: {area:.0f}")

#TASK 5: Write a Python program to calculate the area of a parallelogram.
b = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
area = b * h
print(f"Output: {area}")