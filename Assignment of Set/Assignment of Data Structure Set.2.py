fruitset = {512, "socrates", "darwin", 62.3}
print(fruitset)

print(type(fruitset))
print(len(fruitset))

for i in fruitset:
    print(i)

fruitset.add(77)
print(fruitset)

fruitset.discard(512)
print(fruitset)