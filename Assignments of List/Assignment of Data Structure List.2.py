fruitlist = [101, 'catch me if you can', 'einstein', 75.25]
print(fruitlist)

print(type(fruitlist))
print("total len in fruitlist:", len(fruitlist))

for i in fruitlist:
    print(i)

print(fruitlist[2])
print(type(fruitlist)[2])

fruitlist.append("xyz")
print(fruitlist)

fruitlist.insert(1, 2005)
print(fruitlist)

fruitlist.remove(75.25)
print(fruitlist)

fruitlist.pop(3)
print(fruitlist)