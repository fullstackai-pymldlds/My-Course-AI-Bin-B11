BookYear = 1977
BookPrice = 54.5
Result = BookYear * BookPrice

print(BookYear)
print(BookPrice)
print(Result)

print(type(BookYear))
print(type(BookPrice))
print(type(Result))

if BookPrice > 50:
    print("Greater than 50")
elif BookPrice < 50:
    print("Less than 50")
else:
    print("Equal to 50")

print("This statement always executes")