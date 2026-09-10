toolset = {634, "unity", "galileo", 44.7}
print(toolset)

print(type(toolset))
print(len(toolset))

for i in toolset:
    print(i)

toolset.add(88)
print(toolset)

toolset.discard(634)
print(toolset)