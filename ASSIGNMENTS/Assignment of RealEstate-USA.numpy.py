import numpy as np

mercedes, rangerover, ford, mazda = np.genfromtxt("ASSIGNMENTS/RealEstate-USA.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5), unpack=True, dtype=None)

print(mercedes)
print(rangerover)
print(ford)
print(mazda)

print(np.min(mercedes))

# Zameen.com price  - statistics operations
print("realestate-USA mercedes mean: ", np.mean(mercedes))
print("realestate-USA mercedes average: ", np.average(mercedes))
print("realestate-USA mercedes mod: ", np.median(mercedes))
print("realestate-USA mercedes std: ", np.std(mercedes))
print("realestate-USA mercedes percentile - 25: ", np.percentile(mercedes, 25))
print("realestate-USA mercedes percentile - 75: ", np.percentile(mercedes, 75))
print("realestate-USA mercedes min: ", np.min(mercedes))
print("realestate-USA mercedes max: ", np.max(mercedes))

# Zameen.com price  - maths operations
print("realestate-USA mercedes square: ", np.square(mercedes))
print("realestate-USA mercedes sqrt: ", np.sqrt(mercedes))
print("realesteate-USA mercedes pow: ", np.pow(mercedes,mercedes))
print("realestate-USA mercedes exp: ", np.exp(mercedes))

# Perform basic arithmetic operations
adddition = ford + mazda
subtraction = ford - mazda
multiplication = ford * mazda
division = ford / mazda

print(" realestate-USA ford - mazda - addition: ", adddition)
print(" realestate-USA ford - mazda - subtraction: ", subtraction)
print(" realestate-USA ford - mazda - multiplication: ", multiplication)
print(" realestate-USA ford - mazda - division: ", division)

#Trigonometric Functions

mercedespie = (mercedes/np.pi) +1

# Calculate sine, cosine, and tangent
sine_values = np.sin(mercedespie)
cosine_values = np.cos(mercedespie)
tangent_values = np.tan(mercedespie)

print("realestate-USA mercedes - div - pie - sine values: ", sine_values)
print("realestate-USA mercedes - div - pie - cosine values: ", cosine_values)
print("realestate-USA mercedes - div - pie - tangent values: ", tangent_values)

print("realestate-USA mercedes - div - pie - exponential values: ", np.exp(mercedespie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(mercedespie)
log10_array = np.log10(mercedespie)

print("realestate-USA mercedes - div - pie - natural logarithm values: ", log_array)
print("realestate-USA mercedes - div - pie - base-10 logarithm values: ", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(mercedespie)
print("realestate-USA mercedes - div - pie - hyperbolic sine values: ", sinh_values)

#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(mercedespie)
print("realestate-USA mercedes - div - pie - hyperbolic cosine values: ", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(mercedespie)
print("realestate-USA mercedes - div - pie - hyperbolic tangent values: ", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(mercedespie)
print("realestate-USA mercedes - div - pie - inverse hyperbolic sine values: ", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(mercedespie)
print("realestate-USA mercedes - div - pie - inverse hyperbolic cosine values: ", acosh_values)

#Zameen.com Long Plus Lat - 2 dimentional arrary
d2fordmazda = np.array([ford,      
                    mazda])
print("realestate-USA ford plus mazda - 2 dimensional array: ", d2fordmazda)

# check the dimension of array1
print("realestate-USA ford plus mazda - 2 dimensional array - dimension: ", d2fordmazda.ndim)
# Output: 2

# return total number of elements in array1
print("realestate-USA ford plus mazda - 2 dimensional array - total number of elements: ", d2fordmazda.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("realestate-USA ford plus mazda - 2 dimensional array - give size of array in each dimension: ", d2fordmazda.shape)
# Output: (2,3)

# check the data type of array1
print("realestate-USA ford plus mazda - 2 dimensional array - data type: ", d2fordmazda.dtype)
# Output: int64

# Splicing array
d2fordmazdasplice= d2fordmazda[0:1:1, 1:2:1]
print("realestate-USA ford plus mazda - 2 dimensional array - splicing array - d2fordmazda[0:1, 1:2]: ", d2fordmazdasplice)
D2fordmazdaSlice2= d2fordmazda[0:1, 4:15:4]
print("realestate-USA ford plus mazda - 2 dimensional array - splicing array - D2fordmazdaSlice2[0:1, 4:15:4]: ", D2fordmazdaSlice2)

# Indexing array
D2fordmazdasliceitemonly = D2fordmazdaslice[0,1]
print("realestate-USA ford plus mazda - 2 dimensional array - index array - d2fordmazdaslice[0,1]: ", d2fordmazdasliceitemonly)
D2fordmazdasliceitemonly2 = D2fordmazda[0,4]
print("realestate-USA ford plus mazda - 2 dimensional array - index array - d2fordmazdaslice[0,4]: ", d2fordmazdasliceitemonly)

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2fordmazda):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2fordmazda):
    print(index, elem)

"""# for loop
rows = np.shape(D2fordmazda[0])[0]
cols = np.shape(D2fordmazda[0])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print(D2fordmazda[i][j])
"""
# 2 x 149 ========>>>>> 1  x 298 - reshape
d2fordmazda1to298 = np.reshape(d2fordmazda, (1, 298))
print("realestate-USA ford plus mazda - 2 dimensional array - np.reshape(d2fordmazda, (1, 298)) : ", d2fordmazda1to298)
print("realestate-USA ford plus mazda - 2 dimensional array - np.reshape(d2fordmazda, (1, 298)) : size ", d2fordmazda1to298.size)
print("realestate-USA ford plus mazda - 2 dimensional array - np.reshape(d2fordmazda, (1, 298)) : shape ", d2fordmazda1to298.shape)
print("realestate-USA ford plus mazda - 2 dimensional array - np.reshape(d2fordmazda, (1, 298)) : dimension ", d2fordmazda1to298.ndim)




print()