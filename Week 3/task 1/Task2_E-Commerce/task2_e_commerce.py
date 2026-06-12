"""
## Task 2 — E-Commerce Discount Calculator

### Scenario

An online store wants to show customers how much they saved.

### Concepts Practiced

- Arithmetic operators
- Casting
- Variables
- Formatting

### Requirements

Ask the user for:

- Product name
- Original price
- Discount percentage

Calculate:

- Discount amount
- Final price after discount

### Example

Input:

```python
Laptop
250000
15
```

Output:

```python
===== PURCHASE SUMMARY =====
Product: Laptop
Original Price: ₦250000
Discount: ₦37500
Final Price: ₦212500
```

### Brain Task

You must figure out:

- how percentages work
- how to calculate discount properly

### Checklist

-  Uses arithmetic operators
-  Uses float/int conversion
-  Stores calculations in variables
-  Includes comments

------
"""

print("Welcome to BC E-Commerce Discount Calculator \n Enter Product Details to Calculate Discount")

#Prompt user to enter the required details
product_name = input("Enter the Product Name: ")
original_price = input("Enter Original Price: ")
original_price = float(original_price.replace(",", ""))
discount = float(input("Enter Discount Percentage: "))

#Calculate discount 
discount = discount / 100

#Calculate discount amount and final price
discount_amount = original_price * discount
final_price = original_price - discount_amount
original_price = format(original_price, ",.2f")
discount_amount = format(discount_amount, ",.2f")
final_price = format(final_price, ",.2f")

#Display results
print("===== PURCHASE SUMMARY =====")
print(f"Product: {product_name}")
print(f"Original Price: N{original_price}")
print(f"Discount: N{discount_amount}")
print(f"Final Price: N{final_price}")