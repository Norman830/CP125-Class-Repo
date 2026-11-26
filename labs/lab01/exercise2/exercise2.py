# Lab 01 Exercise 2: Camping Logistics
def calculate_tent_cost(participants,tent_capacity,tent_price):
    tents_needed = -(-participants // tent_capacity)
    total = tents_needed * tent_price
    return total

print(calculate_tent_cost(12,4,100))
print(calculate_tent_cost(13,4,100))