"""
### **Task 2: The Warehouse "Case & Remainder" Calculator**

**Focus:** Arithmetic Operators (Floor Division/Modulo) and Assignment Operators.

**The Scenario:** Our warehouse needs to ship units in large crates (12 units) and small boxes (4 units).

- **The Input:** Ask the user for the total number of units to ship.
- **The Logic:**
  1. Use `//` to find how many full crates are needed.
  2. Use `%` to find the units left over after crates.
  3. Use `//` again to see how many small boxes fit the remainder.
  4. Anything left after that is "Individual Loose Items."
- **The Assignment:** Use an **Assignment Operator** (e.g., `total_cost += ...`) to calculate shipping fees: $50 per crate, $20 per box, and $5 per loose item.
- **Output:** Print the breakdown: `Crates: X, Boxes: Y, Loose: Z. Total Cost: $ABC`.
"""

#Take inout and cast to datatype interger
total_units = int(input("Enter Total number of unit: "))
total_cost = 0

#Get the units of every category
full_crate = total_units // 12
units_left = total_units % 12
small_boxes = units_left // 4
loose_items = units_left % 4

#Calculaye cost for every category
total_cost += full_crate * 50
total_cost += small_boxes * 20
total_cost += loose_items * 5

#Calculate total cost
#total_cost = cost_for_crate + cost_for_box + cost_for_loose_items
# total_cost += cost_for_box, cost_for_box, cost_for_loose_items

#Display Values
print (f"Crates: {full_crate}, Boxex: {small_boxes}, Loose: {loose_items}. Total Cost: ${total_cost}")
