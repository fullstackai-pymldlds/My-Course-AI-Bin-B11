import numpy as np

amazon, google, apple, meta = np.genfromtxt("ASSIGNMENTS/Startup-USA.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5), unpack=True, dtype=None)

print(amazon)
print(google)
print(apple)
print(meta)

print(np.min(amazon))

# Startup-USA amazon (Funding Rounds) - statistics operations
print("Startup-USA amazon mean: ", np.mean(amazon))
print("Startup-USA amazon average: ", np.average(amazon))
print("Startup-USA amazon mod: ", np.median(amazon))
print("Startup-USA amazon std: ", np.std(amazon))
print("Startup-USA amazon percentile - 25: ", np.percentile(amazon, 25))
print("Startup-USA amazon percentile - 75: ", np.percentile(amazon, 75))
print("Startup-USA amazon min: ", np.min(amazon))
print("Startup-USA amazon max: ", np.max(amazon))

# Startup-USA amazon (Funding Rounds) - maths operations
print("Startup-USA amazon square: ", np.square(amazon))
print("Startup-USA amazon sqrt: ", np.sqrt(amazon))
print("Startup-USA amazon pow: ", np.pow(amazon, amazon))
print("Startup-USA amazon exp: ", np.exp(amazon))

# Perform basic arithmetic operations
adddition = apple + meta
subtraction = apple - meta
multiplication = apple * meta
division = apple / meta

print(" Startup-USA apple - meta - addition: ", adddition)
print(" Startup-USA apple - meta - subtraction: ", subtraction)
print(" Startup-USA apple - meta - multiplication: ", multiplication)
print(" Startup-USA apple - meta - division: ", division)

# Trigonometric Functions

amazonpie = (amazon / np.pi) + 1

# Calculate sine, cosine, and tangent
sine_values = np.sin(amazonpie)
cosine_values = np.cos(amazonpie)
tangent_values = np.tan(amazonpie)

print("Startup-USA amazon - div - pie - sine values: ", sine_values)
print("Startup-USA amazon - div - pie - cosine values: ", cosine_values)
print("Startup-USA amazon - div - pie - tangent values: ", tangent_values)

print("Startup-USA amazon - div - pie - exponential values: ", np.exp(amazonpie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(amazonpie)
log10_array = np.log10(amazonpie)

print("Startup-USA amazon - div - pie - natural logarithm values: ", log_array)
print("Startup-USA amazon - div - pie - base-10 logarithm values: ", log10_array)

# Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(amazonpie)
print("Startup-USA amazon - div - pie - hyperbolic sine values: ", sinh_values)

# Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(amazonpie)
print("Startup-USA amazon - div - pie - hyperbolic cosine values: ", cosh_values)

# Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(amazonpie)
print("Startup-USA amazon - div - pie - hyperbolic tangent values: ", tanh_values)

# Example: Inverse Hyperbolic Sine
# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(amazonpie)
print("Startup-USA amazon - div - pie - inverse hyperbolic sine values: ", asinh_values)

# Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(amazonpie)
print("Startup-USA amazon - div - pie - inverse hyperbolic cosine values: ", acosh_values)

# Startup-USA apple plus meta - 2 dimensional array
d2applemeta = np.array([apple,
                        meta])
print("Startup-USA apple plus meta - 2 dimensional array: ", d2applemeta)

# check the dimension of d2applemeta
print("Startup-USA apple plus meta - 2 dimensional array - dimension: ", d2applemeta.ndim)
# Output: 2

# return total number of elements in d2applemeta
print("Startup-USA apple plus meta - 2 dimensional array - total number of elements: ", d2applemeta.size)
# Output: 10000

# return a tuple that gives size of array in each dimension
print("Startup-USA apple plus meta - 2 dimensional array - give size of array in each dimension: ", d2applemeta.shape)
# Output: (2, 5000)

# check the data type of d2applemeta
print("Startup-USA apple plus meta - 2 dimensional array - data type: ", d2applemeta.dtype)

# Splicing array
d2applemetasplice = d2applemeta[0:1:1, 1:2:1]
print("Startup-USA apple plus meta - 2 dimensional array - splicing array - d2applemeta[0:1, 1:2]: ", d2applemetasplice)
d2applemetaslice2 = d2applemeta[0:1, 4:15:4]
print("Startup-USA apple plus meta - 2 dimensional array - splicing array - d2applemetaslice2[0:1, 4:15:4]: ", d2applemetaslice2)

# Indexing array
d2applemetaitemonly = d2applemetasplice[0, 0]
print("Startup-USA apple plus meta - 2 dimensional array - index array - d2applemetasplice[0,0]: ", d2applemetaitemonly)
d2applemetaitemonly2 = d2applemeta[0, 4]
print("Startup-USA apple plus meta - 2 dimensional array - index array - d2applemeta[0,4]: ", d2applemetaitemonly2)

# You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(d2applemeta):
    print(elem)

# If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(d2applemeta):
    print(index, elem)

# 2 x 5000 ========>>>>> 1 x 10000 - reshape
d2applemeta1to10000 = np.reshape(d2applemeta, (1, 10000))
print("Startup-USA apple plus meta - 2 dimensional array - np.reshape(d2applemeta, (1, 10000)) : ", d2applemeta1to10000)
print("Startup-USA apple plus meta - 2 dimensional array - np.reshape(d2applemeta, (1, 10000)) : size ", d2applemeta1to10000.size)
print("Startup-USA apple plus meta - 2 dimensional array - np.reshape(d2applemeta, (1, 10000)) : shape ", d2applemeta1to10000.shape)
print("Startup-USA apple plus meta - 2 dimensional array - np.reshape(d2applemeta, (1, 10000)) : dimension ", d2applemeta1to10000.ndim)

print()