# Logical Operators in Python

var1 = 7
var2 = 5

# AND operator
print("AND operator")
# Condition1 is True, Condition2 is True, Result is True
chkAnd = var1 > var2 and var1 > 6
print(chkAnd)

# Condition1 is True, Condition2 is False, Result is False
chkAnd = var1 > var2 and var1 < 6
print(chkAnd)

# Condition1 is False, Condition2 is True, Result is False
chkAnd = var1 < var2 and var1 > 6
print(chkAnd)

# Condition1 is False, Condition2 is False, Result is False
chkAnd = var1 < var2 and var1 < 6
print(chkAnd)

# OR operator
print("OR operator")
# Condition1 is True, Condition2 is True, Result is True
chkOr = var1 > var2 or var1 > 6
print(chkOr)

# Condition1 is True, Condition2 is False, Result is True
chkOr = var1 > var2 or var1 < 6
print(chkOr)

# Condition1 is False, Condition2 is True, Result is True
chkOr = var1 < var2 or var1 > 6
print(chkOr)

# Condition1 is False, Condition2 is False, Result is False
chkOr = var1 < var2 or var1 < 6
print(chkOr)

# NOT operator
print("NOT operator")
chkNot = not var1==var2
print(chkNot)

chkNot = not var1!=var2
print(chkNot)
