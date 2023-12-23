# Removing values from list in Python

# Creating a list of values
anyList = [1, "Name", 24, "Designation", 55.4, "Active"]
print(anyList)

# Remove last item in list
anyList.pop()
print(anyList)

# Remove item at particular index using pop
anyList.pop(2)
print(anyList)

# Remove item at particular index using del command
del anyList[1]
print(anyList)

# Remove particular value
anyList.remove("Designation")
print(anyList)

# Clears all items in list
anyList.clear()
print(anyList)

# To delete the list itself
del anyList
