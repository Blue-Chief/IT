import math

seconds = 523450 
price_per_dollar = 0.0000153

cost = seconds * price_per_dollar

four_decimal_place_cost = format(cost, ".4f")

cost_round_up = math.ceil(cost)
cost_round_down = math.floor(cost)

print(f"Actual Cost: {four_decimal_place_cost}")
print(f"Rounded Up: {cost_round_up}")
print(f"Rounded Down: {cost_round_down}")