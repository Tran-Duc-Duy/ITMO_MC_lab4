#
# Complete the 'interpolate_by_lagrange' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. DOUBLE_ARRAY x_axis
#  2. DOUBLE_ARRAY y_axis
#  3. DOUBLE x
#
def interpolate_by_lagrange(x_axis, y_axis, x):
    n = len(x_axis)
    y = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L *= (x - x_axis[j]) / (x_axis[i] - x_axis[j])
        y += y_axis[i] * L
    return y

# import numpy as np
# from numpy import double
# import matplotlib.pyplot as plt

# print('This program takes in input, uses Lagrange polynomial to solve for polynomials')

# # Define a function to calculate the Lagrange polynomial
# def lagrange_poly(x_values, function_values, x_point):
#     y_point = 0
#     for x_i, y_i in zip(x_values, function_values):
#         product = np.prod(((x_point - x_values[x_values != x_i])/(x_i - x_values[x_values != x_i])))
#         y_point += y_i * product
#     return y_point

# # Get the degree of the polynomial from the user
# degree = int(input('Enter the degree of the polynomial:\n'))

# # Get the x values and function values from the user
# x_values = np.array(list(map(double,input('Enter x values x(i):\n').strip().split()))[:degree +1], double)
# function_values = np.array(list(map(double,input('Enter functions f(i):\n').strip().split()))[:degree +1], double)

# # Check if user wants to find the function at a particular point
# choice = int(input('Do you also want to know the function at a particular point x? 1 -> yes 0-> no \n'))

# # If user wants to find the function at a particular point, get the value of x
# if choice == 1:
#     x_point = double(input('Enter the value:\n'))
# else:
#     x_point = 0

# # Set x_c to the value of x_point
# x_c = x_point

# # Calculate the solution for x_c using Lagrange polynomial
# y_c = lagrange_poly(x_values, function_values, x_c)

# # Print the solution for x_c
# print(x_c, y_c)

# # Generate x values for plotting
# x_plot = np.linspace(x_values[0], x_values[-1])

# # Calculate y values for plotting
# y_plot = np.array([lagrange_poly(x_values, function_values, x_p) for x_p in x_plot])

# # Plot the function and the point (x_c, y_c)
# plt.plot(x_c, y_c, 'go')

# # Plot the input points and the Lagrange polynomial
# plt.plot(x_values, function_values, 'ro', x_plot, y_plot, 'b-')

# # Add gridlines and labels to the plot
# plt.grid()
# plt.title('Graph of f(x)')
# plt.xlabel('x')
# plt.ylabel('y',rotation=0)

# # Show the plot
# plt.show()