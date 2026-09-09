"""

===========================================================
   LECTURE 01 - SET 03:  TYPE CONVERSION 
   Topics :  TYPE CONVERSION & TYPE CASTING
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:    TYPE CONVERSION (IMPLICIT)
# ==========================================================

# Q1: Divide two Integers.
#    a = 10 , b = 4
#    Find c = a / b , print c and type(c)
#    Also try: 10 / 2 and see the type.
#    (HINT:  / always gives float)

a = 10
b = 4
result = a / b

print("Result =" , result)
print("Type =" , type(result))

c = 10 / 2

print("10 / 2 =" , c)
print("Type =" , type(c))

# ----------------------------------------------------------

# Q2: Add Integer and Boolean.
#    a = 5 , b = True
#    Find c = a + b, print c and type(c)
#    Also try: 5 + False
#    (HINT:  True becomes 1, False becomes 0)

a = 5
b = True
result = a + b

print("5 + True =" , result)
print("Type =" , type(result))

print("5 + False =" , 5 + False)

# ----------------------------------------------------------


# ==========================================================
# PART B:    TYPE CASTING (EXPLICIT)
# ==========================================================
