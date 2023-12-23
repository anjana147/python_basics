# Assigning values to variables by taking input

# Take input from user, default datatype is string
varA = input("Enter value")
print(varA)
print(type(varA))

# Take input from user, convert datatype to int
varB = int(input("Enter value"))
print(varB)
print(type(varB))

# Take input from user, convert datatype to float
varC = float(input("Enter value"))
print(varC)
print(type(varC))

# Take input from user and print, note that the value is not saved in memory
print(input("Enter value"))

varX, varY, varZ = input("Enter string value"), int(input("Enter int value")), float(input("Enter float value"))
print(varX, varY, varZ)
print(type(varX),type(varY),type(varZ))
