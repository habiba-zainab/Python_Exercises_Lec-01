"""

===========================================================
   LECTURE 01 - SET 01 : BASICS OF PYTHON
   Topics : Character Set, Variables, Rules of Identifiers
   Total Questions :
============================================================

"""
# ==========================================================
# PART A:   CHARACTER SET
# ==========================================================

# Q1: Print a simple Python banner using letters, digits and
#     special characters.

print("=== WELCOME TO PYTHON ===  >>>  LET'S CODE!")

# ----------------------------------------------------------

# Q2: Create a simple name tag using different character 
#      types in PYTHON's character set.

print("+----------------------+")
print("|  NAME: Habiba Zainab |")
print("|  year: 2026          |")
print("+----------------------+")

# ----------------------------------------------------------

# Q3: Print examples of  weak and passwords showing different
#      character types.

print("WEAK Password:  abc123 (only letters + digits)")
print("STRONG Password: Ch@racter_2026! (letters + digits + special chars)")

# ----------------------------------------------------------

# ==========================================================
# PART B:   VARIABLES
# ==========================================================

# Q4: Create variables to store your personal information
#    Create: name (string), age (integar), height (float), 
#    is_student (boolean).
#    Print all variables with labels.

name = "Habiba Zainab"
age = 18
height = 5.4
is_student = True

print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("is_student: ", is_student)

# ----------------------------------------------------------

# Q5: Variable reassignment and tracking 
#    Start with: counter = 0
#    Increment counter by 5
#    Increment counter by 10
#    Increment counter by 15
#    Print counter value after each increment.

counter = 0
print("Initial: " + str(counter))

counter += 5
print("After +5: " + str(counter))

counter += 10
print("After +10: " + str(counter))

counter += 15
print("After +15: " + str(counter))

# ----------------------------------------------------------

# Q6: Swap two variables without using a third variable.
#    Start with: x = 5, y = 10
#    After swap: x should be 10, y should be 5
#    Print both before and after swapping.

