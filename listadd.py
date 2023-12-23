# Adding values in list in Python

# Creating a list of values
anyList = [1, "Name", 24, "Designation", 55.4]

# Add a value to an index of existing list
anyList.insert(3, "Active")
print(anyList)

# Appending a value to a list
anyList.append(1985)
print(anyList)

# Appending elements from a list to existing list
thisList = ["Kochi", "Kerala", 682310]
anyList.extend(thisList)
print(anyList)
