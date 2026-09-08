"""

===========================================================
   LECTURE 01 - SET 02:  DATA-TYPES and OPERATORS
   Topics : Data-Types & Types of Operators
   Total Questions :  
============================================================

"""
# ==========================================================
# PART A:    DATA-TYPES
# ==========================================================

# Q1: Create ONE variable of each data type:
#    int, float, str, bool, None
#    Print the Value and the Type of each one.

my_int = 42
my_float = 3.14
my_str = "Welcome"
my_bool = True
my_none = None

print("INTEGER: ", my_int, "| Type: ", type(my_int))
print("FLOAT: ", my_float, "| Type: ", type(my_float))
print("STRING: ", my_str, "| Type: ", type(my_str))
print("BOOLEAN: ", my_bool, "| Type: ", type(my_bool))
print("NONE: ", my_none, "| Type: ", type(my_none))

# ----------------------------------------------------------

# Q2: Create a variable with value "100" (string). Convert it to:
#    Integar    
#    Float
#    Print original and converted values with their types.

num_str = "100"

num_int = int(num_str)
num_float = float(num_str)

print("Original: ", num_str, "| Type: ", type(num_str))
print("As Integer: ", num_int, "| Type: ", type(num_int))
print("As Float: ", num_float, "| Type: ", type(num_float))

# ----------------------------------------------------------

# Q3: Create variables to store shopping data using different 
#    data types:
#   Product name (string)
#   Quantity (integer)
#   Price (float)
#   Is available (boolean)
#   Print them in a formatted manner.

name = "Laptop"
quantity = 3
price = 899.99
in_stock = True

print("=" * 30)
print("     PRODUCT DETAILS")
print("=" * 30)
print("Item Name: ", name)
print("Quantity: ", quantity)
print("Price: ", price)
print("Available: ", in_stock)
print("=" * 30)

# ----------------------------------------------------------

# ==========================================================
# PART B:    OPERATORS
# ==========================================================


# Q4: ARITHEMATIC OPERATOR
#    Take two numbers from the user and print:
#    Sum, Difference, Product, Division, Remainder, Power.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum: ", num1 + num2)
print("Difference: ", num1 - num2)
print("Product: ", num1 * num2)
print("Division: ", num1 / num2)
print("Remainder: ", num1 % num2)
print("Power: ", num1 ** num2)

# ----------------------------------------------------------

# Q5: COMPARISON OPERATOR
#    Take two numbers and print the result of:
#    == , != , > , < , >= , <= .

a = float(input("Enter a: "))
b = float(input("Enter b: "))

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# ----------------------------------------------------------
