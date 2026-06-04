from datetime import datetime, timedelta, date
import math

"""
**The Scenario:** A Project Manager needs a tool to estimate the end date of a task based on work hours, avoiding weekends.

**Requirements:**

1. **User Inputs:**
   - Project Start Date (Format: `YYYY-MM-DD`).
   - Total Estimated Work Hours (Integer).
   - Hourly Rate (Float).
2. **Calculation:**
   - Calculate the total cost of the project (Hours × Rate).
   - Calculate the number of **workdays** needed (assume exactly 8 hours of work per day).
3. **The Deadline Logic:**
   - Add the number of workdays to the start date to find the "Project Completion Date."
   - **The Brain-Tasker:** If the calculated completion date falls on a **Saturday** or **Sunday**, your script must automatically increment the date to the **following Monday**.
4. **Output:**
   - Display the total cost formatted to 2 decimal places with a currency symbol.
   - Display the final completion date in a readable format (e.g., `Monday, May 18, 2026`).
"""

print("BC Project Management Tool")
print("Input Project Start Date, Total Estimated Work Hours (8 hrs per day) and Hourly Rate(pay)")
print(" ")

psd = datetime.strptime(input("Project Start Date: "), "%Y-%m-%d").date()

work_hours = int(input("Total Estimated Work Hours: "))
#pay_rate = f"{(float(input("Hourly Rate: "))):.2f}"
pay_rate = float(input("Hourly Rate: "))
pay_rate = format(pay_rate, ".2f")
print(f"Hourly Rate: {pay_rate} ")

cost_of_project = f"{(int(work_hours) * float(pay_rate)):.2f}"
work_days = (work_hours) / 8

#Approximating work_days to the next whole number because even if 1 hour falls in another day, its still a full day
work_days = math.ceil(work_days)

#Convert datetime to integer
#psdi = int(psd.strftime("%Y%m%d"))
#psdi = psdi - 1
psdii = psd - timedelta(days = 1)
psdi = timedelta(days=work_days)

#Calculate project completion date 
pcd = psdi + psdii
print(f"Total Work days: {work_days}")

#Convert back to datetime
#pcdf =  datetime.strptime(str(pcd), "%Y%m%d").date()

#If it falls on either Saturday or Sunday
if pcd.strftime("%A") == "Saturday":
    pcd = pcd + timedelta(days=2)
elif pcd.strftime("%A") == "Sunday":
    pcd = pcd + timedelta(days=1)

#Format for Day of the week and May 18th, 2026
day_date = pcd.strftime("%A")
final_date = pcd.strftime("%B %d, %Y")

print(" ")
#Display results
print(f"Total Cost of project: ${cost_of_project:,}")
print(f"Date of Completion of task: {day_date}, {final_date}")
