from datetime import datetime, date, timedelta 
import math

"""
**The Scenario:** You are building a CLI tool for the front desk to bill clients for refreshments and parking.

**Requirements:**

1. **User Inputs:**
   - Number of guests (e.g., `6`).
   - Cost per refreshment (e.g., `12.50`).
   - Arrival Time and Departure Time (Use 24-hour format: `HH:MM`).
2. **The Logic:**
   - **Refreshment Subtotal:** `Guests * Price`.
   - **Bulk Discount:** If guests > 5, apply a 10% discount to the refreshment subtotal.
   - **Parking Fee:** Parking costs **₦5.00 per hour**. You must charge for a full hour even if they stay for a fraction of an hour (e.g., 1 hour and 10 minutes = 2 hours charged).
3. **The Brain-Tasker (Formatting):**
   - Generate a "Receipt" in the terminal.
   - You must use **string alignment** (`<`, `>`, or `^`) to ensure that all prices align vertically, regardless of the length of the label.
   - Apply a final 7.5% Service Tax to the grand total.
"""
print("BC Front Desk Tool")
print("Input number of guests, cost of refreshment, Arrival Time and Departure Time")
print(" ")

guests = int(input("Number of Guests: "))
price = format(float(input("Cost per Refreshment: ")), ".2f")
arrival_time = datetime.strptime(input("Arrival Time: "), "%H:%M")
departure_time = datetime.strptime(input("Departure Time: "), "%H:%M")
#cars = int(input("Number of Cars: "))

#After a little code review, I found out that format(word, ".2f") is stored as a string
refreshment_subtotal = int(guests) * float(price)
refreshment_subtotal = format(refreshment_subtotal, ".2f")

#Convert time spent to float using .total_seconds() and approximate to (int) using math.ceil()
time_spent = (departure_time - arrival_time)
time_spent = math.ceil(time_spent.total_seconds()/3600)

#Calculate the 10 percent discount
if guests > 5:
    refreshment_subtotal = float(refreshment_subtotal) * 0.9
else:
  refreshment_subtotal = int(guests) * float(price)

#Calculate the cost per parking
if guests > 0:
    parking_fee = guests * time_spent * 5

#Calculate Service tax
service_tax = (refreshment_subtotal + parking_fee) * 0.075
service_tax = format(service_tax, ".2f")

#Calculate grand total
total_due = refreshment_subtotal + parking_fee + float(service_tax)
total_due = format(total_due, ".2f")

print(f"====================================")
print(f"|  |  |   OFFICE RECEIPT")
print(f"====================================")
print(f"Refreshments:   {'N':>7}   {refreshment_subtotal:>5}")
print(f"Parking Fee:    {'N':>7}   {parking_fee:>5}")
print(f"Tax (7.5%):     {'N':>7}   {service_tax:>5}")
print(f"------------------------------------")
print(f"TOTAL DUE:      {'N':>7}   {total_due:>5}")
print(f"====================================")