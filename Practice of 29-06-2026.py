# WELCOME TO PRACTICE SESSION OF 29 JUNE 2026

MobileName = input("Enter your mobile name: ") #Enter Name
print(MobileName)

print(type(MobileName))

print(len(MobileName))

for X in MobileName:
    print(X)

#My First Code Ends Here

MobilePrice = input("Enter your mobile price: ")
print(MobilePrice)

print(type(MobilePrice))

print(len(MobilePrice))

for X in MobilePrice:
    print(X)

MobilePrice = float(input("Enter your mobile price: "))
print(MobilePrice)

print(type(MobilePrice))

if MobilePrice > 5:
    print("Greater than 5")
elif MobilePrice < 5:
    print("Less than 5")
elif MobilePrice < 3:
    print("Less than 3")
else:
    print("WhatEver...")