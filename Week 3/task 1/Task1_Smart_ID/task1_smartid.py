"""
## Task 1 — Smart Identity Card Generator

### Scenario

A company wants every intern to have a generated identity code.

### Concepts Practiced

- Strings
- Slicing
- String methods
- Concatenation

### Requirements

Ask the user for:

- First name
- Last name
- Year of birth

Generate an ID using:

- First 2 letters of first name
- Last 2 letters of last name
- Last 2 digits of birth year
- Convert everything to uppercase

### Example

Input:

```python
Samuel
Johnson
2003
```

Output:

```python
SAON03
```

### Brain Task

Figure out how to extract:

- first characters
- last characters
- last digits

### Checklist

-  Uses slicing correctly
-  Uses `.upper()`
-  Uses concatenation
-  Includes comments

------
"""

print("Identity Code Generation System")
print("Provide your First Name, Last Name and Year of Birth")
print(" ")

#Prompt User to enter the required details
first_name = input("Enter your First Name: ").strip()
last_name = input ("Enter your Last Name: ").strip()
yob = input("Enter your Year of Birth: ").strip()

#Extracting needed details to generte ID
f_n = first_name[:2]
l_n = last_name[-2:]
y_o_b = yob[-2:]

#joining the required details that have been extracted and converting to uppercase
id = (f_n + l_n + y_o_b).upper()

print(id)
print(f"{first_name}, your ID is {id}")