# Accessing values in list in Python

# Creating a list of values
anyList = [1, "Name", 24, "Designation", 55.4]

# Accessing items at any particular index
print(anyList[0])
print(anyList[2])

# Accessing range of items from position 1 to 3, note that end index should be n+1
print(anyList[1:4])

# Accessing range of items from position start index to 2
print(anyList[:3])

# Accessing range of items from position 2 to end index
print(anyList[2:])

# Negative indexing
print(anyList[-5:-1])
