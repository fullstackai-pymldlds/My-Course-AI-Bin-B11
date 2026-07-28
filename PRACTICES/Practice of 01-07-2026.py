import numpy as NP

Mercedes, RangeRover, Ford, Mazda = NP.genfromtxt('RealEstate-USA.csv', delimiter=',', usecols=(2,3,4,5), unpack=True, dtype='str')

print(Mercedes)
print(RangeRover)
print(Ford)
print(Mazda)

print(NP.min(Mercedes))
print(NP.min(RangeRover))
print(NP.min(Ford))
print(NP.min(Mazda))