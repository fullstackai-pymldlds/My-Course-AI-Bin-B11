import numpy as np

mcdonalds, subway = np.genfromtxt("ASSIGNMENTS/Restaurants-USA.csv", delimiter=",", skip_header=1, usecols=(4, 5), unpack=True, dtype=float, invalid_raise=False)

print(mcdonalds)
print(subway)

print(np.min(mcdonalds))

# Restaurants-USA latitude - statistics operations
print("Restaurants-USA mcdonalds mean: ", np.mean(mcdonalds))
print("Restaurants-USA mcdonalds average: ", np.average(mcdonalds))
print("Restaurants-USA mcdonalds mod: ", np.median(mcdonalds))
print("Restaurants-USA mcdonalds std: ", np.std(mcdonalds))
print("Restaurants-USA mcdonalds percentile - 25: ", np.percentile(mcdonalds, 25))
print("Restaurants-USA mcdonalds percentile - 75: ", np.percentile(mcdonalds, 75))
print("Restaurants-USA mcdonalds min: ", np.min(mcdonalds))
print("Restaurants-USA mcdonalds max: ", np.max(mcdonalds))

# Restaurants-USA latitude - maths operations
print("Restaurants-USA mcdonalds square: ", np.square(mcdonalds))
print("Restaurants-USA mcdonalds sqrt: ", np.sqrt(np.abs(mcdonalds)))
print("Restaurants-USA mcdonalds pow: ", np.pow(mcdonalds, 2))
print("Restaurants-USA mcdonalds exp: ", np.exp(mcdonalds))

# Perform basic arithmetic operations
adddition = mcdonalds + subway
subtraction = mcdonalds - subway
multiplication = mcdonalds * subway
division = mcdonalds / subway

print(" Restaurants-USA mcdonalds - subway - addition: ", adddition)
print(" Restaurants-USA mcdonalds - subway - subtraction: ", subtraction)
print(" Restaurants-USA mcdonalds - subway - multiplication: ", multiplication)
print(" Restaurants-USA mcdonalds - subway - division: ", division)

# Trigonometric Functions

mcdonaldspie = (np.abs(mcdonalds) / np.pi) + 1

# Calculate sine, cosine, and tangent
sine_values = np.sin(mcdonaldspie)
cosine_values = np.cos(mcdonaldspie)
tangent_values = np.tan(mcdonaldspie)

print("Restaurants-USA mcdonalds - div - pie - sine values: ", sine_values)
print("Restaurants-USA mcdonalds - div - pie - cosine values: ", cosine_values)
print("Restaurants-USA mcdonalds - div - pie - tangent values: ", tangent_values)

print("Restaurants-USA mcdonalds - div - pie - exponential values: ", np.exp(mcdonaldspie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(mcdonaldspie)
log10_array = np.log10(mcdonaldspie)

print("Restaurants-USA mcdonalds - div - pie - natural logarithm values: ", log_array)
print("Restaurants-USA mcdonalds - div - pie - base-10 logarithm values: ", log10_array)

# Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(mcdonaldspie)
print("Restaurants-USA mcdonalds - div - pie - hyperbolic sine values: ", sinh_values)

# Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(mcdonaldspie)
print("Restaurants-USA mcdonalds - div - pie - hyperbolic cosine values: ", cosh_values)

# Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(mcdonaldspie)
print("Restaurants-USA mcdonalds - div - pie - hyperbolic tangent values: ", tanh_values)

# Example: Inverse Hyperbolic Sine
# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(mcdonaldspie)
print("Restaurants-USA mcdonalds - div - pie - inverse hyperbolic sine values: ", asinh_values)

# Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(mcdonaldspie)
print("Restaurants-USA mcdonalds - div - pie - inverse hyperbolic cosine values: ", acosh_values)

# Restaurants-USA latitude plus longitude - 2 dimensional array
d2mcdonaldssubway = np.array([mcdonalds,
                              subway])
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array: ", d2mcdonaldssubway)

# check the dimension of d2mcdonaldssubway
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - dimension: ", d2mcdonaldssubway.ndim)
# Output: 2

# return total number of elements in d2mcdonaldssubway
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - total number of elements: ", d2mcdonaldssubway.size)

# return a tuple that gives size of array in each dimension
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - give size of array in each dimension: ", d2mcdonaldssubway.shape)

# check the data type of d2mcdonaldssubway
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - data type: ", d2mcdonaldssubway.dtype)

# Splicing array
d2mcdonaldssubwaysplice = d2mcdonaldssubway[0:1:1, 1:2:1]
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - splicing array - d2mcdonaldssubway[0:1, 1:2]: ", d2mcdonaldssubwaysplice)
d2mcdonaldssubwayslice2 = d2mcdonaldssubway[0:1, 4:15:4]
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - splicing array - d2mcdonaldssubwayslice2[0:1, 4:15:4]: ", d2mcdonaldssubwayslice2)

# Indexing array
d2mcdonaldssubwayitemonly = d2mcdonaldssubwaysplice[0, 0]
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - index array - d2mcdonaldssubwaysplice[0,0]: ", d2mcdonaldssubwayitemonly)
d2mcdonaldssubwayitemonly2 = d2mcdonaldssubway[0, 4]
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - index array - d2mcdonaldssubway[0,4]: ", d2mcdonaldssubwayitemonly2)

# You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(d2mcdonaldssubway):
    print(elem)

# If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(d2mcdonaldssubway):
    print(index, elem)

# 2 x 9990 ========>>>>> 1 x 19980 - reshape
d2mcdonaldssubway1to19980 = np.reshape(d2mcdonaldssubway, (1, 19980))
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - np.reshape(d2mcdonaldssubway, (1, 19980)) : ", d2mcdonaldssubway1to19980)
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - np.reshape(d2mcdonaldssubway, (1, 19980)) : size ", d2mcdonaldssubway1to19980.size)
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - np.reshape(d2mcdonaldssubway, (1, 19980)) : shape ", d2mcdonaldssubway1to19980.shape)
print("Restaurants-USA mcdonalds plus subway - 2 dimensional array - np.reshape(d2mcdonaldssubway, (1, 19980)) : dimension ", d2mcdonaldssubway1to19980.ndim)

print()