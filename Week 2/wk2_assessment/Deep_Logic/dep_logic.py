"""
### **Task 3: The "Deep-Logic" Loan Qualifier**

**Focus:** Logical Operators (`and`, `or`, `not`) and Comparison.

**The Scenario:** You are building the backend for a FinTech app. A user only qualifies for a loan under specific, tricky conditions.

- **The Input:** Ask for `Age`, `Credit Score`, and `Monthly Income`.
- **The Logic:** A user is `is_qualified` **ONLY IF**:
  1. They are at least 21 years old.
  2. **AND** they have a credit score above 700.
  3. **OR** they have a credit score above 600 **AND** an income over $5,000.
  4. **AND NOT** if their income is less than $1,500 (regardless of score).
- **The Goal:** The interns must write this entire logic in **one single line** of code using parentheses and logical operators.
- **Output:** `Loan Qualification Status: True/False`.
"""

print("Welcome to BC Money Loan App")

age = int(input("Enter your Age: "))
credit_score = int(input("Enter your Credit Score: "))
monthly_income = float(input("Enter your Monthly Income: "))
monthly_income = format(monthly_income, ".2f")
monthly_income = float(monthly_income)

# # if (age >= 21 and credit_score > 700 and monthly_income > 1500) or (age >= 21 and credit_score > 600 and monthly_income > 5000):

# #if age >= 21 and credit_score > 700  or (credit_score > 600 and monthly_income > 5000) and not monthly_income > 1500:
if (age >= 21) and ((credit_score > 700 or (credit_score > 600 and monthly_income > 5000)) and not (monthly_income  < 1500)):
     print(f"Loan Qualification Status: {True}")
else:
     print(f"Loan Qualification Status: {False}")

