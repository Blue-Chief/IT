"""
### **Task 4: The Membership "Promo Code" Masker**

**Focus:** Strings, Booleans, and Comparison Operators.

**The Scenario:** A user enters a promo code. We need to check if it's valid and hide part of it for security.

- **The Input:** A promo code (e.g., `SAVE2026-XYZ`).
- **The Logic:**
  1. Check if the code starts with `"SAVE"` (Boolean).
  2. Check if the total length is exactly 12 characters.
  3. **The Operators:** Use a **Logical Operator** to ensure both conditions are met.
- **The String Mask:** If valid, show the first 4 characters, then four `*`, then the last 2 characters (e.g., `SAVE****YZ`).
- **Output:** Display the masked code and a Boolean `is_valid` status.
Refactor
"""

promo_code = input ("Enter Promo Code: ")

start_len = 4
end_len = 2
#middle_len = len(promo_code) - (start_len + end_len)    
start = promo_code[:start_len]
end = promo_code[-end_len:]
middle = "*" * 4

code = start + middle + end

if promo_code.startswith("SAVE") and len(promo_code) == 12:
    print("Status: Valid")

else:
    print ("Status: Invalid")

print(code)

