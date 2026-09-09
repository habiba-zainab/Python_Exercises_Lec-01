"""

============================================================
   LECTURE 01 - SET 04:  MINI CHALLENGE
   Topics :  All Topics are included
============================================================

"""
# ===========================================================
#         SIMPLE SHOPPING CALCULATOR
# ===========================================================

# ----------------------------------------------------------
#    STEP 01:     Welcome Message
# ----------------------------------------------------------

print("*** wELCOME TO QUICK SHOP ***")
print("=" , 35)

# ----------------------------------------------------------
#     STEP 02:    Store Customer & Produuct Information
# ----------------------------------------------------------

shop_name = "QuickMart"
customer_name = "Kevin"
customer_id = "K3V!N"
item1_name = "Laptop"
item2_name = "Mouse"
item3_name = "Keyboard"

print(f"\nShop: {shop_name}")
print(f"Customer: {customer_name}")
print(f"Customer ID: {customer_id}")

# ----------------------------------------------------------
#     STEP 03:    Set Prices & Quantities
# ----------------------------------------------------------

item1_price = "45000"        
item2_price = "500.50"       
quantity1 = 2
quantity2 = 1
tax_rate = 18.0
price3 = 1200.0
is_member = True
has_coupon = False
items_list = ["Laptop", "Mouse", "Keyboard"]

print(f"\nItem 1: {item1_name} - ₹{item1_price}")
print(f"Item 2: {item2_name} - ₹{item2_price}")
print(f"Item 3: {item3_name} - ₹{price3}")

# ----------------------------------------------------------
#     STEP 04:    Convert String Prices to Numbers
# ----------------------------------------------------------

print("\n--- Converting Prices ---")
print(f"Before: item1_price = '{item1_price}' (string)")

price1 = float(item1_price)
price2 = float(item2_price)

print(f"After: price1 = {price1} (float)")
print(f"After: price2 = {price2} (float)")

# ----------------------------------------------------------
#     STEP 05:    Calculate Item Totals
# ----------------------------------------------------------

print("\n--- Items Purchased ---")
print(f"1. {item1_name}: ₹{price1} × {quantity1}")
print(f"2. {item2_name}: ₹{price2} × {quantity2}")
print(f"3. {item3_name}: ₹{price3} × 1")

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * 1

print(f"\nItem 1 Total: ₹{total1}")
print(f"Item 2 Total: ₹{total2}")
print(f"Item 3 Total: ₹{total3}")

# ----------------------------------------------------------
#     STEP 06:    Calculate Subtotal
# ----------------------------------------------------------

subtotal = total1 + total2 + total3

print(f"\nSubtotal: ₹{subtotal}")