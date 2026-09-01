citylist = [212, 'wings of fire', 'newton', 33.4]
print(citylist)

print(type(citylist))
print("total len in citylist:", len(citylist))

for i in citylist:
    print(i)

print(citylist[2])
print(type(citylist)[2])

citylist.append("lmn")
print(citylist)

citylist.insert(1, 1990)
print(citylist)

citylist.remove(33.4)
print(citylist)

citylist.pop(3)
print(citylist)