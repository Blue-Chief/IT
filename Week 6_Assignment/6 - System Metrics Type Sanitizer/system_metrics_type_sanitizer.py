values = [82, "91", None, 45, "Error", 73.5]

new_values = []

for value in values:
    if isinstance (value, (int, float)):
        new_values.append(value)
    elif value is None:
        continue
    else:
        try:
            new_values.append(float(value))
        except TypeError as err:
            print(f"{err}")
            continue
        except ValueError as err:
            print(f"{err}")
            continue
        
total = 0

for value in new_values:
    total += value

avg = total / len(new_values)

print(f"The Total Sum is {total}")
print(f"The Average is {avg}")
print(new_values)