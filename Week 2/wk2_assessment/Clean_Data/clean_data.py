"""
### **Task 1: The "Clean-Room" Data Entry Engine**

**Focus:** Casting, Strings, and Membership Operators.

**The Scenario:** A client sent a CSV-style string where prices are messy. You must clean the data and validate if it belongs to a "Premium" category.

- **The Input:** Ask the user to input a product record in this format: `Laptop : $1,200.50` (Note the spaces and symbols).
- **The Logic:**
  1. Use string methods to remove the `$` and `,`.
  2. Cast the cleaned price to a **float** and the product name to **lowercase**.
  3. Define a list (or string) of "luxury_keywords" like `"laptop, smartphone, camera"`.
- **The Operators:** Use a **Membership Operator** (`in`) to check if the input product is in your luxury list and a **Comparison Operator** to check if the price is `> 1000`.
- **Output:** Return a Boolean value (`True/False`) stating if the item is a "High-Value Electronic."
"""

print("Enter Product Record Using this Format - Laptop : $1,200.50")

#Accept input from User
product_record = input("Product Record: ")

#We remove some keywords by using the replace function
cleaned_product_record = product_record.replace("$", "").replace(",", "")

#We split the list and cast the index of 1 to float
cleaned_price = float(cleaned_product_record.split(":")[1].strip())

#We assign the first index to a new variable name and convert to lowercase
cleaned_product_name = cleaned_product_record.split(":")[0].lower().strip()

#Define list of luxury items
luxury_keywords = ["laptop", "smartphone", "camera", "electric car", "headset", "smartwatch"]

print(cleaned_price)
print(cleaned_product_name)

if cleaned_product_name in luxury_keywords and cleaned_price > 1000:
    print(f"{True}, This is a High-Value Electronic")
else:
    print(f"{False}, This is a Low-Value Electronic")
