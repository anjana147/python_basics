# Changing values in list in Python

# Creating a list of values
anyList = [1, "Name", 24, "Designation", 55.4]
print("Before changing Name ", anyList)

# Changing value at any index
anyList[1] = "FirstName LastName"
print("After changing Name ", anyList)

# Changing range of values
anyList[2:4] = [25, "Promoted", 57.3]
print("After changing Age, Designation, Weight", anyList)

# Inserting more values into a range
anyList[1:2]=["FirstName LastName","Mother's Maiden Name"]
print("After inserting more items than replaced",anyList)

# Inserting less values into a range
anyList[1:3]=["FirstName SurName"]
print("After inserting less items than replaced",anyList)
